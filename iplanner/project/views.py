from .serializers import *
from rest_framework import generics
from .models import *
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
import requests
from bs4 import BeautifulSoup
from rake_nltk import Rake

from rest_framework import status
from rest_framework.parsers import FileUploadParser

class project_details(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ProjectSerializer
    queryset = Project.objects.all()


class projects(generics.ListCreateAPIView):
    serializer_class = ProjectSerializer
    def get_queryset(self):
        user = self.kwargs['user']
        return Project.objects.filter(user=user)


class project_file_upload(APIView):
    parser_classes = (FileUploadParser,)

    def post(self, request, filename, project, object_type, object_id, user, type, format=None):

        # project = int(project)
        # if project == 0:
        #     project=None

        user_obj = User.objects.get(pk=user)

        file_obj = request.data['file']
        try:
            if int(project) == 0:


                project_file = ProjectFile.objects.create(project_file=file_obj, object_type=object_type,
                                                          object_id=object_id, name=filename, type=type, user=user_obj)

            else:
                project_obj = Project.objects.get(pk=project)
                project_file = ProjectFile.objects.create(project_file=file_obj, project=project_obj, object_type=object_type, object_id=object_id,
                                                       user=user_obj, name=filename, type=type)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        else:

            serializer = ProjectFileSerializer(instance=project_file, context={'request': request})
            print(serializer.data)
            return Response(serializer.data)




class project_image_upload(APIView):
    parser_classes = (FileUploadParser,)

    def put(self, request, filename, pk, format=None):

        file_obj = request.data['file']


        project_image = Project.objects.get(pk=pk)
        project_image.image = file_obj


        try:
            project_image.save()
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        else:


            serializer = ProjectSerializer(project_image, context={'request': request})

            return Response(serializer.data)


class project_file_details(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ProjectFileSerializer
    queryset = ProjectFile.objects.all()


class project_files(generics.ListCreateAPIView):
    serializer_class = ProjectFileSerializer
    # lookup_field = 'project'
    def get_queryset(self):
        project = self.kwargs['project']
        return ProjectFile.objects.project(project)

class project_files_by_type(generics.ListCreateAPIView):
    serializer_class = ProjectFileSerializer
    def get_queryset(self):
        project = self.kwargs['project']
        type = self.kwargs['type']
        return ProjectFile.objects.project(project).type(type)

class project_files_by_object(generics.ListAPIView):
    serializer_class = ProjectFileSerializer
    def get_queryset(self):
        object_id = self.kwargs['object_id']
        object_type = self.kwargs['object_type']
        project =  int(self.kwargs['project'])
        if project == 0:
            project=None

        print(project)
        return ProjectFile.objects.filter(project=project, object_type = object_type, object_id = object_id)

class project_files_guery(generics.ListCreateAPIView):
    serializer_class = ProjectFileSerializer
    def get_queryset(self):
        project = self.kwargs['project']


        query = self.kwargs['query']
        return ProjectFile.objects.project(project).search(query)


class project_competitor_details(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ProjectCompetitorSerializer
    queryset = ProjectCompetitor.objects.all()


class project_competitors(generics.ListCreateAPIView):
    serializer_class = ProjectCompetitorSerializer

    def get_queryset(self):
        project = self.kwargs['project']
        return ProjectCompetitor.objects.filter(project=project)


class project_competitor_move_down(APIView):


    def get_object(self, pk):
        return get_object_or_404(ProjectCompetitor, id=pk)


    def put(self, request, pk):
        position = self.get_object(pk)

        position.move_down()
        serializer = ProjectCompetitorSerializer(position)

        return Response(serializer.data)


class project_competitor_move_up(APIView):
    def get_object(self, pk):
        return get_object_or_404(ProjectCompetitor, id=pk)

    def put(self, request, pk):
        position = self.get_object(pk)

        position.move_up()
        serializer = ProjectCompetitorSerializer(position)

        return Response(serializer.data)


class project_mockup_details(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ProjectMockupSerializer
    queryset = ProjectMockup.objects.all()


class project_mockups(generics.ListCreateAPIView):
    serializer_class = ProjectMockupSerializer

    def get_queryset(self):
        project = self.kwargs['project']
        return ProjectMockup.objects.filter(project=project)


class project_mockup_file_details(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ProjectMockupFilesSerializer
    queryset = ProjectMockupFiles.objects.all()


class project_mockup_files(generics.ListCreateAPIView):
    serializer_class = ProjectMockupFilesSerializer

    def get_queryset(self):
        mockup = self.kwargs['mockup']
        return ProjectMockupFiles.objects.filter(project_mockup=mockup)


class project_team_list(generics.ListCreateAPIView):
    serializer_class = ProjectTeamSerializer
    def get_queryset(self):
        project = self.kwargs['project']
        return ProjectTeam.objects.filter(project=project)


class project_team_member(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ProjectTeamSerializer
    queryset = ProjectTeam.objects.all()


class user_projects_list(generics.ListCreateAPIView):
    serializer_class = ProjectTeamdetailsSerializer
    def get_queryset(self):
        user = self.kwargs['user']
        return ProjectTeam.objects.filter(user=user)



class website_keywords_analysis(APIView):


    def get(self, request, competitor):




        obj = ProjectCompetitor.objects.get(pk=competitor)
        site_url = obj.url
        domain = get_domain_name(site_url)


        links_on_page = get_website_hrefs(site_url,domain)

        links_on_page.append(obj.url)
        links_on_page.append(domain)
        links_on_page = list(set(links_on_page))
        titles = []
        descriptions = []
        title_key_words = []
        description_key_words = []
        h1_tags = []
        h1_key_words = []
        p_texts = []
        p_key_words = []
        second_links = []

        i=0
        for url in links_on_page:
            i=i+1
            if i<100:
                second_links = second_links + get_website_hrefs(url, domain)

        second_links = list(set(second_links))

        links_on_page = links_on_page + second_links

        links_on_page = list(set(links_on_page))

        for url in links_on_page:
             # todo check norobots, noindex
            page = requests.get(url)
            soup = BeautifulSoup(page.text, 'html.parser')

            if soup.title:
                titles.append(soup.title.string)
                title_key_words = title_key_words + extract_keywords(soup.title.string)

            desc = soup.find(attrs={"name": "description"})
            if desc:
                descriptions.append(desc['content'].strip())
                description_key_words = description_key_words + extract_keywords(desc['content'].strip())

            h1 = soup.find('h1')
            if h1:
                h1_tags.append(h1.text.strip())
                h1_key_words = h1_key_words + extract_keywords(h1.text.strip())
                # p = h1.find_next('p')
                # if p:
                #     p_texts.append(p.text.strip())
                #     p_key_words = p_key_words + extract_keywords(p.text.strip())



        data = {
            'title': titles,
            'description': descriptions,
            'h1': h1_tags,
            'p': p_texts,
            'id': 1,
            'title_key_words': title_key_words,
            'description_key_words': description_key_words,
            'h1_keywords': h1_key_words,
            'p_keywords': p_key_words,
            'urls':links_on_page
        }
        # result = soup.findAll(attrs={"name":"description"})
        # data = {
        #     'text': result[0]['content'].encode('utf-8'),
        #     'id': 1,
        # }



        return Response(data)

def get_website_hrefs (site_url, index_url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.9; rv:45.0) Gecko/20100101 Firefox/45.0'
    }



    page = requests.get(site_url, headers = headers)

    soup = BeautifulSoup(page.text, 'html.parser')

    collect = soup.find('body')
    hrefs = collect.findAll('a')

    links_on_page = []
    for link in hrefs:
        url = link.get('href')

        if url:
            if url not in ["/", "#"] and "@" not in url and "#" not in url and 'javascript' not in url \
                    and 'contact' not in url and 'career' not in url and 'vacancy' not in url \
                    and 'image' not in url and '.jpeg' not in url and '.gif' not in url \
                    and '.jpg' not in url and '.png' not in url:
                if (index_url in str(url) and str(url) not in [index_url, index_url + '/']) \
                        or ('http' not in str(url)):
                    if 'http' not in str(url) and url[0:2]!='www':
                        if url[0] == '/':
                            links_on_page.append(index_url  + str(url))
                        else:
                            links_on_page.append(index_url + '/' + str(url))
                    else:
                        if url.count('http')==1 or url.count('www')==1:
                            links_on_page.append(str(url))

    links_on_page= list(set(links_on_page))
    return links_on_page

def extract_keywords (text):
    r = Rake()
    r.extract_keywords_from_text(str(text))
    return r.get_ranked_phrases()

def get_domain_name (site_url):

    f = site_url.find('//')
    l = len(site_url)
    d = site_url[f + 2:l]
    f1 = d.find('/')

    if f1 == -1:
        domein = site_url
    else:
        domein = site_url[0:f1 + f + 2]

    return domein