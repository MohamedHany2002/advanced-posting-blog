from django.shortcuts import render,get_object_or_404,redirect,HttpResponseRedirect,reverse
from .models import post,comment
from django.core.paginator import Paginator, EmptyPage,PageNotAnInteger
from django.views.generic import ListView
from django.core.mail import send_mail
from .forms import email_form
from taggit.models import Tag
from django.db.models import Count
from django.views.generic import ListView


# Create your views here.


# class PostList(ListView):
#     model = post
#     template_name = 'blog/home.html'
#     context_object_name = 'posts'
#     paginate_by=3

# include pagination with page=page_obj

def post_list(request,tag_slug=None):
    posts=post.published_posts.all()
    all_tags=Tag.objects.all()
    tag=None
    if tag_slug:
        tag=get_object_or_404(Tag,slug=tag_slug)
        posts=posts.filter(tags__in=[tag])
    ###### pagination
    paginator = Paginator(posts, 3) # 3 posts in each page
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    print(posts,"posts")
    ###
    return render(request,"blog/home.html",{'posts':posts,'page':page,'tag':tag,'all_tags':all_tags})

def post_detail(request,slug):

    # try to use another example with aggregate without any previous filtering
    desired_post=get_object_or_404(post,slug=slug)
    newcomment=False
    similar_posts=desired_post.tags.similar_objects()
    # tags_related_ids=desired_post.tags.values_list('id',flat=True)
    # tags_related_ids=desired_post.tags.all()
    # print(tags_related_ids)
    # similar_posts=post.objects.filter(tags__in=tags_related_ids).exclude(id=desired_post.id).distinct()
    # for mypost in similar_posts:
    #     print(mypost,mypost.tags.all().count())
    # print('//')

    # each post has some tags and i want annotate these
    # similar_posts=similar_posts.aggregate(Count('tags'))
    # for sipost in similar_posts:
    #     print(sipost,sipost.mytags)
    # print('//s')
    # norposts=post.objects.annotate(number=Count('tags'))
    # for nor in norposts:
    #     print(nor,nor.number)
    
    # similar_posts=desired_post.tags.similar_objects()   
    # for minepost in similar_posts:
    #     print(minepost,minepost.mytags__count)
    

    # post_dict={}
    # for related_tag in tags_related:
    #     if not related_tag in post_dict:
    #         post_dict[related_tag]=0
    #     else:
    #         post_dict[related_tag]+=1

    
    # print(post_dict)
    # posts=post.objects.filter(tags__in=tags_related).exclude(id=desired_post.id)
    if request.method=='POST':
        text=request.POST['text']
        comment.objects.create(text=text,user=request.user,post=desired_post)
        newcomment=True
        # desired_post.post_comments.add()
    comments=desired_post.post_comments.filter(active=True)
    return render(request,"blog/detail.html",{'similar_posts':similar_posts,'post':desired_post,'comments':comments,'newcomment':newcomment})




# class list_posts(ListView):
#     model=post
#     query_set=post.published_posts.all()
#     context_object_name='posts'
#     paginate_by=3
#     template_name='blog/home.html'

def sending_email(request,id):
    mypost=post.objects.get(id=id)
    sent=False
    if request.method=='POST':
        myform=email_form(request.POST)
        if myform.is_valid():
            post_url=request.build_absolute_uri(mypost.get_absolute_url())
            print("ok",post_url)
            subject="posted that post {}".format(mypost.title)
            body="posted that post {} and includeing the link {}".format(mypost.body,post_url)
            mail=myform.cleaned_data['email']
            send_mail(subject,body,'goldenhany94@gmail.com',[mail])
            print('mail sent ')
            sent=True
    else:    
        myform=email_form()
    return render(request,"blog/send_mail.html",{'form':myform,'post':mypost,'sent':sent})


# def comment_post(id):
#     mypost=get_object_or_404(post,id=id)
#     text=request.POST['text']
#     lolo=comment.objects.create(text=text,user=request.user,post=mypost)
#     # return HttpResponseRedirect(reverse("detail",kwargs={'slug':mypost.slug}))
#     return render(request,"blog/detail.html",{'toto':lolo})



# def details(request,id):
#     mypost=get_object_or_404(post,id=id)
#     post_tag_ids=mypost.tags.values_list('id',flat=True)
#     similarposts=post.objects.filter(tags__in=post_tag_ids)
#     similarposts=similarposts.annotate(tag_count=Count('tags')).order_by('-tag_count')
