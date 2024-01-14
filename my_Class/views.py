from django.shortcuts import render,get_object_or_404,redirect
from django.http import HttpResponse
from django.template import loader
from .models import *
from django.utils import timezone
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required

from datetime import datetime
from .forms import *
from django.contrib.auth.views import LoginView
from django.http import JsonResponse





classroom = Class.objects.get(class_CODE='6A')
# view lớp học
@login_required(login_url='/home/')
def classroom_view(request):
  now = datetime.now()
  class_code = request.session.get('class_code', None)
  subject_code = request.GET.get('subject_code', None)
  # subject_code = request.GET.get('subject_code')
  request.session['subject_code'] = subject_code
  # print(class_code)
  # print(subject_code)
  if subject_code is not None:
    subject = get_object_or_404(Subject, subject_CODE=subject_code)
  else:
    subject = "Chưa lấy được"
    print(request.session.items())
  classroom = Class.objects.get(class_CODE=class_code)
  students = Student.objects.filter(classroom=classroom)
  template = loader.get_template('classroom.html')
  
  if request.method == 'POST':
    form_lession = LessonsForm(request.POST)
    if form_lession.is_valid():
      form_lession.save()
      return redirect('Classroom') 
  else:
    form_lession = LessonsForm()
  if request.method == 'POST':
      form_review = LessonReviewForm(request.POST)
      if form_review.is_valid():
          form_review.save()
          return redirect('classroom') 
  else:
      form_review = LessonReviewForm()
  context = {
      'class':classroom,
      'Students' : students,
      'current_time':now,
      'subject_code': subject,
      'form_add_lesssion': form_lession,
      'form_review': form_review
  }
  return HttpResponse(template.render(context,request))

#  view đăng kí 
def register_view (request):
  form = RegistrationForm()
  template = loader.get_template('register.html')
  if request.method == 'POST':
    form = RegistrationForm(request.POST)
    if form.is_valid():
      form.save()
      return HttpResponseRedirect('/')
  context = {
    'form': form
  }
  return HttpResponse(template.render(context,request))

def student_detail(request, student_ID):
  # lấy student, lưu vào session
  student = get_object_or_404(Student, pk=student_ID)
  request.session['student_ID'] = student_ID
  # Lấy subject_code từ session
  subject_code = request.session.get('subject_code')
  subject = get_object_or_404(Subject,pk=subject_code)
  # Hiển thị bảng điểm
  scores = Score.objects.filter(student=student,subject =subject_code)
  my_student = Student.objects.get(student_ID=request.session['student_ID'])
  my_subject = Subject.objects.get(subject_CODE=request.session['subject_code'])
  print(my_student)
  print(subject)
  if request.method == 'POST':
      form = ScoreForm_Test(request.POST)
      if form.is_valid():
        try:
          score = form.save(commit=False)
          score.student = my_student
          return redirect('student_detail')  # replace with your success url
        except Exception as e:
          print(f"An error occurred: {e}")
  else:
        form = ScoreForm_Test()
  template = loader.get_template('details.html')
  context = {
    'student': student,
    'scores': scores,
    'form': form
  }
  return HttpResponse(template.render(context,request))



  
class CustomLoginView(LoginView):
  authentication_form = CustomLoginForm

  def get_context_data(self, **kwargs):
      context = super().get_context_data(**kwargs)
      context['form_student_ID'] = StudentIDForm()
      return context
  def post(self, request, *args, **kwargs):
      form = StudentIDForm(request.POST)
      if form.is_valid():
          student_id = form.cleaned_data['student_id']
          return redirect('student_grade_view', student_ID=student_id)
      else:
          return super().post(request, *args, **kwargs)

def student_grade_view(request, student_ID):
  student = get_object_or_404(Student, pk=student_ID)
  scores = Score.objects.filter(student=student)
  template = loader.get_template('student_grade.html')
  context = {
    'student': student, 
    'scores': scores
  }
  return HttpResponse(template.render(context,request))


def week_summary_view(request):
  reviews = LessonReview.objects.all()  # Lấy tất cả đánh giá
  template = loader.get_template('week_summary.html')
  context = {
    'week_review':reviews
  }
  return HttpResponse(template.render(context,request))

  
def option_view(request):
  # xử lí select class and subject
  classes = Class.objects.all()
  subjects = None
  if 'class_code' in request.GET:
    class_code = request.GET.get('class_code')
    try:
      classroom = Class.objects.get(class_CODE=class_code)
      subjects = list(classroom.subjects.values())
      request.session['class_code'] = class_code  
    except Class.DoesNotExist:
      pass
    return JsonResponse(subjects, safe=False)
  else:
    return render(request, 'option.html', {'classes': classes})


def create_lesson_view(request):
    if request.method == 'GET':
        subject_code = request.GET.get('subject_code')
        if subject_code:
            try:
                # Lấy thông tin từ session và request
                teacher_username = request.session.get('username')
                class_code = request.session.get('class_code')

                # Lấy đối tượng từ cơ sở dữ liệu
                teacher = Teacher.objects.get(username=teacher_username)
                classroom = Class.objects.get(class_CODE=class_code)
                subject = Subject.objects.get(subject_CODE=subject_code)

                # Tạo một Lesson mới
                lesson = Lessons(classroom=classroom, subject=subject, teacher=teacher, schedule_time=timezone.now())
                lesson.save()

                return HttpResponse('Lesson created successfully')
            except (Teacher.DoesNotExist, Class.DoesNotExist, Subject.DoesNotExist):
                return HttpResponse('Failed to create lesson: invalid data')
        else:
            return HttpResponse('Failed to create lesson: no subject_code provided')
    else:
        return HttpResponse('Invalid request method')
      


def test_saveScore (request):
  form=ScoreForm_Test()
  template = loader.get_template('test.html')
  if request.method == 'POST':
        form = ScoreForm_Test(request.POST)
        if form.is_valid():
            form.save()
            return redirect('test_Savescore')
  else:
        form = ScoreForm_Test()
 
  context = {
    'form': form
  }
  return HttpResponse(template.render(context,request))


# input điểm 
def save_score(request):
  template = loader.get_template('details.html')
  student_id = request.session.get('student_ID')
  get_student = get_object_or_404(Student, Student_ID=student_id)
  subject_id = request.session.get('subject_id')
  get_subject = get_object_or_404(Subject, id=subject_id)
  # Kiểm tra xem request có phải là POST không
  if request.method == 'POST':
    form = ScoreForm_Test(request.POST)
    if form.is_valid():
        form.save()
        return redirect('test')
  else:
    form = ScoreForm_Test()
  context = {
    'form': form
  }
  return HttpResponse(template.render(context,request))


  
def lesson_review(request, lesson_id):
    lesson = get_object_or_404(Lessons, pk=lesson_id)
    if request.method == 'POST':
        form = LessonReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.lesson = lesson
            review.save()
            return redirect('classroom', lesson_id=lesson.id)  # replace with your success url
    else:
        form = LessonReviewForm()
    return render(request, 'classroom.html', {'form_review': form, 'lesson': lesson})