from django.db import models

# Create your models here.
class Doctor(models.Model):
    name = models.TextField()

    def __str__(self):
        return f'{self.name} 전문의'
    
    
class Patient(models.Model):
    # 환자 모델에 ManyToManyField 작성
    doctors = models.ManyToManyField(Doctor, through='Reservation')  # Reservation이라는 테이블을 통해 MTM을 맺을 것이다
    name = models.TextField()
    # doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE) 중개모델을 사용한다면 필요 없어짐

    def __str__(self):
        return f'{self.pk}번 환자 {self.name}'

# ========중개모델==================
# 예약테이블
# class Reservation(models.Model):
#     doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
#     patient = models.ForeignKey(Patient, on_delete=models.CASCADE)

#     def __str__(self):
#         return f'{self.doctor_id}번 의사의 {self.patient_id}번 환자'

# 중개테이블 만들기
class Reservation(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    
    # id 말고 다른 값들
    symptom = models.TextField()
    reserved_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.doctor.pk}번 의사의 {self.patient.pk}번 환자'