from django.shortcuts import render

def kahitano(request):

    context = {
        'user' : 'Cheska',
        'paragraph' : 'Video provides a powerful way to help you prove your point. When you click Online Video,\
        you can paste in the embed code for the video you want to add. You can also type a keyword to search online for the video that best fits your document. \
        To make your document look professionally produced, Word provides header, footer, cover page, and text box designs that complement each other. For example,\
        you can add a matching cover page, header, and sidebar.',

        'paragraph1' : 'Video provides a powerful way to help you prove your point. When you click Online Video,\
        you can paste in the embed code for the video you want to add. You can also type a keyword to search online for the video that best fits your document. \
        To make your document look professionally produced, Word provides header, footer, cover page, and text box designs that complement each other. For example,\
        you can add a matching cover page, header, and sidebar.',

        'x' : 50

    }
    return render(request, 'aaa.html', context)
# Create your views here.
