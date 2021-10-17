from contacts.models import Contact, Role
from django.contrib.auth.models import User


contact1 = Contact(id='1', name='Helen', email='lala@example.com')
contact2 = Contact(id='2', name='Pieter', email='pieter@example.com')
contact3 = Contact(id='3', name='Jane', email='jane@example.com')
contact4 = Contact(id='4', name='Kan', email='kan@example.com')
contact5 = Contact(id='5', name='Kate', email='kate@example.com')


contact1.save()
contact2.save()
contact3.save()
contact4.save()
contact5.save()

user1 = User.objects.create_user(username="User1", password="111")
user2 = User.objects.create_user(username="User2", password="222")
user3 = User.objects.create_user(username="User3", password="333")

user1.save()
user2.save()
user3.save()

role1 = Role(user=user1, permission="ReadOnly")
role2 = Role(user=user2, permission="ReadAdd")
role3 = Role(user=user3, permission="ReadAddDelete")

role1.save()
role2.save()
role3.save()
