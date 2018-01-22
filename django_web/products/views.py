from django.shortcuts import render
from channels import Group
from django.http import HttpResponse


def sendmessageview(request):
    print("Send product-ace8652aff1f11e78be50ed5f89f718b")
    Group("product-%s" % "ace8652aff1f11e78be50ed5f89f718b").send({
        "text": "Data from view",
    })
    return HttpResponse("Set data to channels")

