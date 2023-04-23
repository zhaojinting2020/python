from django.shortcuts import render

def resume(request):
    context = {
        'name': 'Your Name',
        'avatar': 'https://example.com/avatar.jpg',
        'email': 'you@example.com',
        'phone': '+1 (555) 123-4567',
        'address': '123 Main Street, Anytown USA',
        'education': [
            {
                'degree': 'Bachelor of Science in Computer Science',
                'university': 'University of Example',
                'date': 'May 2023'
            },
            {
                'degree': 'High School Diploma',
                'university': 'Anytown High School',
                'date': 'May 2019'
            },
        ],
        'skills': [
            'Python',
            'Django',
            'JavaScript',
            'HTML',
            'CSS',
        ],
        'introduction': 'I am a software developer with experience in Python, Django, and web development. I am passionate about creating high-quality, scalable software solutions that solve real-world problems.',
    }
    return render(request, 'resume.html', context)