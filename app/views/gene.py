#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 19-8-4 
# @Author  : JiaoJianglong


import re
import requests
from bs4 import BeautifulSoup

from flask import Blueprint, request, render_template, views
from flask_login import login_required

from app.extensions import mongo

gene = Blueprint('gene', __name__)


@gene.route("/message/", methods=["GET", "POST"])
@login_required
def message():
    if request.method == "POST":
        search_text = request.values.get("message")
        limit = int(request.values.get("limit", "10"))
        offset = int(request.values.get("offset", "0"))
        res = requests.get(
            "https://asia.ensembl.org/Multi/Ajax/search?q=(+{0}%5E316+AND+species%3A%22CrossSpecies%22+)"
            "+OR+(+{0}%5E190+AND+species%3A%22Human%22+)+OR+(+{0}%5E80+AND+species%3A%22Mouse%22+)"
            "+OR+(+{0}+AND+species%3A%22Zebrafish%22+)"
            "&fq=(++(++species%3A%22CrossSpecies%22+AND+(+reference_strain%3A1+)++)"
            "++OR++(++species%3A%22Human%22+AND+(+reference_strain%3A1+)++)"
            "++OR++(++species%3A%22Mouse%22+AND+(+reference_strain%3A1+)++)"
            "++OR++(++species%3A%22Zebrafish%22+AND+(+reference_strain%3A1+)++)++)"
            "&hl=true&hl.fl=_hr&hl.fl=content&hl.fl=description&hl.fragsize=500&rows={1}&start={2}"
                .format(search_text, limit, offset)).json()
        response = res.get('result', {}).get("response", {})
        response['total'] = response.get("numFound")
        return response
    return render_template("gene.html")


@gene.route("/transcripts/", methods=["GET", "POST"])
@login_required
def transcripts():
    def parse(value):
        base_url = "https://asia.ensembl.org"
        new_value = {}
        for key, td in value.items():
            try:
                if key == "Name":
                    new_value[key] = td.text
                # elif key == "Translation ID":
                #     new_value[key] = td.a.text
                elif key == "Transcript ID":
                    new_value[key] = {"text": td.a.text, "url": base_url+td.a.attrs["href"]}
                    new_value["_id"] = td.a.text
                elif key == "bp":
                    new_value[key] = td.text
                elif key == "Protein":
                    new_value[key] = {"text": td.a.text, "url": td.a.attrs["href"]}
                elif key == "Biotype":
                    if td.find("span", class_="_ht_tip"):
                        note = td.find("span", class_="_ht_tip").text
                        text = td.find("span", class_="ht _ht").text.replace(note, "")
                    else:
                        text = td.find("div", class_="coltab-text").text
                        note = None
                    color = td.find("span", class_="coltab-tab").attrs["style"]
                    color = re.search(r"background-color:(.*);", color).group(1)
                    new_value[key] = {"text": text, "note": note, "color": color}

                elif key == "CCDS":
                    new_value[key] = {"text": td.a.text, "url": td.a.attrs["href"]}
                elif key == "UniProt":
                    new_value[key] = {"text": td.a.text, "url": td.a.attrs["href"]}
                elif key == "RefSeq Match":
                    new_value[key] = {"text": td.a.text, "url": td.a.attrs["href"]}

                elif key == "Flags":
                    flags = []
                    for span in td.find_all("span", class_="ts_flag"):
                        note = span.find("span", class_="_ht_tip").text
                        text = span.find("span", class_="ht _ht").text.replace(note, "")
                        flags.append({"text": text, "note": note})
                    new_value[key] = flags
            except:
                new_value[key] = None
        return new_value

    suc_result = {"data": "", "code": 200, "msg": "请求成功"}
    if request.method == "GET":
        domain = request.values.get("domain")
        domain_url = request.values.get("domain_url")

        res = requests.get(domain + "/" + domain_url)
        soup = BeautifulSoup(res.text, 'lxml')
        transcripts_table = soup.find(id='transcripts_table')

        keys = [th.text for th in transcripts_table.thead.tr.find_all("th")]
        values = [dict(zip(keys, [td for td in tr.find_all("td")])) for tr in transcripts_table.tbody.find_all("tr")]

        suc_result['data'] = [parse(value) for value in values]

        mongo.db.transcripts.insert_many(suc_result['data'])
        return suc_result
