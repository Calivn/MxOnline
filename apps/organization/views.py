from django.shortcuts import render
from django.views.generic.base import View

from .models import CourseOrg, City


class OrgView(View):
    """
    课程机构列表
    """
    def get(self, request):
        org_nums = CourseOrg.objects.count()    # 机构总数
        all_orgs = CourseOrg.objects.all()      # 所有的课程机构
        all_citys = City.objects.all()      # 所有的城市
        return render(request, "org-list.html", {
            "all_orgs": all_orgs,
            "all_citys": all_citys,
            "org_nums": org_nums
        })
