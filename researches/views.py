from django.shortcuts import render
from .models import ResearchLine, Publication

# Create your views here.
def research_lines(request):
    research_lines = ResearchLine.objects.all()
    return render(request, 'researches/research_lines.html', {'research_lines': research_lines})

def publications(request):
    publications = Publication.objects.all()
    print(publications[0].authors)
    return render(request, 'researches/publications.html', {'publications': publications})
