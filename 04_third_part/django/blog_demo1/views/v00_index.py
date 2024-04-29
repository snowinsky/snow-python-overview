from django.views import View
from django.shortcuts import render

class IndexView(View):
    def get(self, request):
        # 2.接收用户点击的分类id
        cat_id = request.GET.get("cat_id", 1)
        # 3.根据分类id进行分类的查询
        try:
            category = ArticleCategory.objects.get(id=cat_id)
        except ArticleCategory.DoesNotExist:
            return HttpResponseNotFound("没有此分类")
        # 4.获取分页参数
        page_num = request.GET.get("page_num", 1)
        page_size = request.GET.get("page_size", 10)
        # 5.根据分类信息查询文章数据
        articles = Article.objects.filter(category=category)
        # 6.创建分页器
        paginator = Paginator(articles, page_size)
        # 7.进行分页处理
        try:
            page_articles = paginator.page(page_num)
        except EmptyPage:
            return HttpResponseNotFound("empty page")
        # 8. 获取总页数
        total_page = paginator.num_pages
        # 9.组织数据传递给模板
        template_params = {
            "categories": ArticleCategory.objects.all(),
            "category": category,
            "articles": articles,
            "page_articles": page_articles,
            "total_page": total_page,
            "page_size": request.GET.get("page_size", 10),
            "page_num": request.GET.get("page_num", 1),
        }
        return render(request, template_name="index.html", context=template_params)
