from django.shortcuts import render
context = {
'name' : 'Krishnapriya A.M',
'gender':'female',
'role' : 'Aspiring Python Django Developer',
'contact' : ['krish.eyyani1992@gmail.com','+91 8139885947','Thrissur,Kerala'],
'social_site' : ['GitHub','LinkedIn'],
'summary' : "Experienced in building CRUD applications, working with SQL databases, and implementing authentication and REST concepts. Eager to contribute to scalable, efficient web solutions while continuously enhancing technical skills.",
'education' : ['Vidya Academy of Science and Technology','Bachelor of Technology in Computer Science & Engineering [2010-2014]'],
'certifications' : ['Certification in AI Driven Python Programming -Illinois Institute of Technology (Illinois Tech), USA','Python Programming with Django - Entri Elevate , NSDC'],
'gained_val' : ['Gained hands-on experience with Django framework, including models, views, templates, URL routing, forms, and authentication.',
'Built CRUD-based web applications using Django and integrated SQL databases for data storage and management.','Learned backend development concepts such as MVC/MVT architecture, REST principles, and server-side logic implementation'],
'project1' : ['Restaurant Menu Management System (CLI-Based)','Designed and developed a CLI application using Python for managing restaurant menu operations.'],
'project1_desc' : ['Implemented CRUD operations (Create, Read, Update, Delete) using SQLite3 database.','Designed database schema for storing menu items, prices, and availability.','Ensured efficient data handling, input validation, and error handling.','Strengthened understanding of backend logic and database connectivity.'],
'technical_skills':['Programming Language','Web Technologies','Web Frameworks','Database'],
'ProgrammingLanguage':['Python','Javascript','SQL'],
'WebTechnologies':['HTML','CSS','REST APIs'],
'WebFrameworks':['Django(Basics)','Django ORM'],
'Database':['SQLite3','SQL(CRUD Operations)'],
'work_experience1' :'White Hat Junior - Programming Instructor [ Remote ]',
'work_role1':['Designed engaging and simple Lesson plans.','Encouraged logical and creative thinking.','Guided students through several hands-on projects.'],
'work_experience2':'Syntel Private Ltd - Support Associate [ Chennai ]',
'work_role2':['Worked on a critical data integration and quality improvement support project for the American Express Business Card analytic platform.','Oversaw data anomalies, resolved ingestion defects, and optimized ETL workflows to ensure accurate card transactions.'],
}
# Create your views here.
def showResume(request):
	return render(request,'resumepage.html',context)

