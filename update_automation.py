from bs4 import BeautifulSoup
import json
import re

# Projects
projects = json.load(open("projects.json","r"))
work = json.load(open("work_projects.json","r"))
job = json.load(open("jobs.json","r"))
edu = json.load(open("education.json","r"))

# Personal Projects HTML Tag
count = 0
view_details = ''
for p in projects:
    title = p['title']
    icon = p['icon']
    subtitle = p['subtitle']
    data_target = p['data_target']
    id = p['data_target'][1:]
    full_pic = p['full_pic']
    details = p['details']
    tech = p['tech']
    github = p['github']

    if count == 0:
        div_class = '   <div class = "item active">'
        slider = """
                <ol class="carousel-indicators mt-30">
                    <li data-target="#projects" data-slide-to="0" class="active"></li> """
    else:
        div_class = div_class + '   <div class="item">'
        slider = slider + f"""
                    <li data-target="#projects" data-slide-to={count}></li>"""
    
    div_class = div_class + f"""
        <div class="col-sm-7">
            <img class="img-responsive center-block mb-30"
                src={icon} alt={title}
                style="width:200px;height:200px;">
        </div>
        <div class="col-sm-5">
            <div class="carousel-caption card" style="background-color: #F2DACB">
                    <h3>{title}</h3>
                    <h4>{subtitle}</h4>
                    <button class="btn td-btn small outline green" data-toggle="modal"
                    data-target="{data_target}">View
                    Details</button>
            </div>
        </div>
    </div>
    """
    details_content = "<ul>"
    for x in details:
        details_content = details_content + f"""
                                    <li>{x}
                                    </li>
        """
    details_content = details_content + " </ul>"

    tech_stack = """ <p class="mb-30">"""
    for y in tech:
        tech_stack = tech_stack + f"""
                                    <span class="label tag">{y}</span>
    """
    tech_stack = tech_stack + " </p>"
    if github == "Yes":
        link = p['link']
        tech_stack = tech_stack + f"""
                                        <a class="btn td-btn outline green mb-30"
                                    href={link}
                                    target="_blank" title="Link to GitHub"><span
                                        class="glyphicon glyphicon-link"></span> Visit
                                    GitHub</a>
    """
    view_details = view_details + f"""
    <!--View Details Modal-->
        <div class="modal fade" id={id} tabindex="-1" role="dialog" aria-labelledby="rbTitle">
            <div class="modal-dialog wide" role="document">
                <div class="modal-content">
                    <div class="modal-header">
                        <button type="button" class="close" data-dismiss="modal" aria-label="Close"><span
                                aria-hidden="true">&times;</span></button>
                        <h4 class="modal-title text-center" id="rbTitle">Project Details</h4>
                    </div><!-- /.modal-header -->
                    <div class="modal-body">
                        <div class="row">
                            <div class="col-xs-12 bg-star-g">
                                <img class="img-responsive center-block hero" src={full_pic}
                                     style="width:350px;height:200px;">
                            </div>
                        </div>
                        <div class="row">
                            <div class="col-sm-12 text-center">
                                <h3>{title}</h3>
                                <h4>{subtitle}</h4>
                            </div>
                        </div>
                        <div class="row">
                            <div class="col-sm-10 col-sm-offset-1 col-lg-6 col-lg-offset-0">
                                {details_content}
                            </div>
                            <div class="col-sm-10 col-sm-offset-1 col-lg-6 col-lg-offset-0 md-center">
                                <p><strong>Technologies Used:</strong></p>
                                <p class="mb-30">
                                    {tech_stack}
                                </p>
                            </div>
                        </div><!-- /.row -->
                        <div class="modal-footer center">
                            <button type="button" class="btn td-btn outline small" data-dismiss="modal">Close
                                Project</button>
                        </div><!-- /.modal-footer -->
                    </div><!-- /.modal-body -->
                </div><!-- /.modal-content -->
            </div><!-- /.modal-dialog -->
        </div><!-- /.modal -->
    """
    count =+ 1

# Work Projects HTML Tag
count = 0
view_details1 = ''
for w in work:
    title = w['title']
    icon = w['icon']
    subtitle = w['subtitle']
    data_target = w['data_target']
    id = w['data_target'][1:]
    full_pic = w['full_pic']
    details = w['details']
    tech = w['tech']

    if count == 0:
        div_class1 = '   <div class = "item active">'
        slider1 = """
                <ol class="carousel-indicators mt-30">
                    <li data-target="#projects" data-slide-to="0" class="active"></li> """
    else:
        div_class1 = div_class1 + '   <div class="item">'
        slider1 = slider1 + f"""
                    <li data-target="#projects" data-slide-to={count}></li>"""
    
    div_class1 = div_class1 + f"""
        <div class="col-sm-7">
            <img class="img-responsive center-block mb-30"
                src={icon} alt={title}
                style="width:200px;height:200px;">
        </div>
        <div class="col-sm-5">
            <div class="carousel-caption card" style="background-color: #F2DACB">
                    <h3>{title}</h3>
                    <h4>{subtitle}</h4>
                    <button class="btn td-btn small outline green" data-toggle="modal"
                    data-target="{data_target}">View
                    Details</button>
            </div>
        </div>
    </div>
    """

    details_content = "<ul>"
    for x in details:
        details_content = details_content + f"""
                                    <li>{x}
                                    </li>
        """
    details_content = details_content + " </ul>"

    tech_stack = """ <p class="mb-30">"""
    for y in tech:
        tech_stack = tech_stack + f"""
                                    <span class="label tag">{y}</span>
    """
    tech_stack = tech_stack + " </p>"
    view_details1 = view_details1+ f"""
    <!--View Details Modal-->
        <div class="modal fade" id={id} tabindex="-1" role="dialog" aria-labelledby="rbTitle">
            <div class="modal-dialog wide" role="document">
                <div class="modal-content">
                    <div class="modal-header">
                        <button type="button" class="close" data-dismiss="modal" aria-label="Close"><span
                                aria-hidden="true">&times;</span></button>
                        <h4 class="modal-title text-center" id="rbTitle">Project Details</h4>
                    </div><!-- /.modal-header -->
                    <div class="modal-body">
                        <div class="row">
                            <div class="col-xs-12 bg-star-g">
                                <img class="img-responsive center-block hero" src={full_pic}
                                     style="width:350px;height:200px;">
                            </div>
                        </div>
                        <div class="row">
                            <div class="col-sm-12 text-center">
                                <h3>{title}</h3>
                                <h4>{subtitle}</h4>
                            </div>
                        </div>
                        <div class="row">
                            <div class="col-sm-10 col-sm-offset-1 col-lg-6 col-lg-offset-0">
                                {details_content}
                            </div>
                            <div class="col-sm-10 col-sm-offset-1 col-lg-6 col-lg-offset-0 md-center">
                                <p><strong>Technologies Used:</strong></p>
                                <p class="mb-30">
                                    {tech_stack}
                                </p>
                            </div>
                        </div><!-- /.row -->
                        <div class="modal-footer center">
                            <button type="button" class="btn td-btn outline small" data-dismiss="modal">Close
                                Project</button>
                        </div><!-- /.modal-footer -->
                    </div><!-- /.modal-body -->
                </div><!-- /.modal-content -->
            </div><!-- /.modal-dialog -->
        </div><!-- /.modal -->
    """
    count =+ 1

# Job HTML tags
job_details = ''
for j in job:
    date = j['date']
    title = j['title']
    company = j['company']
    details = j['details']
    experience = '<ul>'
    for z in details:
        experience = experience + f"""
                                    <li>{z}</li>
        """
    experience = experience + "</ul>"
    job_details = job_details + f"""
                        <div class="row mb-15">
                            <div class="col-md-2 col-lg-2 col-lg-offset-1">
                                <p class="year"><h6>{date}</h6></p>
                            </div>
                            <div class="col-md-9 col-lg-8">
                                <p class="mb-0"><strong>
                                        <h5>{title}</h5><h6>{company}</h6>
                                    </strong></p>
                            <h6>{experience}</h6>
                            </div>
                        </div>
    """

# Education HTML tags
edu_details = ''
for e in edu:
    date = e['date']
    name = e['name']
    college = e['college']
    gpa = e['GPA']

    edu_details = edu_details + f"""
                                <div class="row mb-15">
                                    <div class="col-md-2 col-lg-2 col-lg-offset-1">
                                        <p class="year"><h6>{date}</h6></p>
                                    </div>
                                    <div class="col-sm-9 col-md-8">
                                        <p class="mb-0"><strong>
                                            <h5>{name}</h5>
                                        </strong></p>
                                        <p><h6>{college}</h6></p>
                                        <p><h6>Grade: {gpa}</h6></p>
                                    </div>
                                </div>
    """

# Edit on the template
with open('template.html', 'r+') as f:
    lines = f.readlines()
    for i, line in enumerate(lines):
        if line.__contains__('<!--PERSONAL PROJECT INSETION HERE-->'):   
            lines[i] = lines[i] + div_class
        if line.__contains__('<!-- PERSONAL PROJECTS SLIDERS -->'):
            lines[i] = lines[i] + slider
        if line.__contains__('<!--WORK PROJECT INSETION HERE-->'):  
            lines[i] = lines[i] + div_class1
        if line.__contains__('<!-- WORK PROJECTS SLIDERS -->'):
            lines[i] = lines[i] + slider1
        if line.__contains__('<!-- PROJECT DETAILS HERE -->'):
            lines[i] = lines[i] + view_details
        if line.__contains__('<!-- PROJECT DETAILS HERE -->'):
            lines[i] = lines[i] + view_details1
        if line.__contains__('<!-- WORK EXPERIENCE INSERTION HERE -->'):
            lines[i] = lines[i] + job_details
        if line.__contains__('<!-- EDUCATION INSERTION HERE -->'):
            lines[i] = lines[i] + edu_details


with open('index.html', 'w') as file:
    file.truncate()
    file.seek(0)
    for line in lines:
        file.write(line)


