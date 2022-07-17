# MayaSchool
An school management system.

# Goal
[Build a Highly Effective School Management System](https://www.nexxushub.com/blog/10-features-of-a-highly-effective-school-management-system)

# TODO
- [ ] front-end
    - [x] login page
    - [x] base page
    - [ ] profile
        - [ ] photo
        - [ ] password
    - [x] dashboard menu (admin, registrar, accountant)
        - [x] see number of student
        - [x] see number of class
        - [x] see number of staff
        - [x] see income
    - [ ] student menu (admin, registrar)
        - [ ] add/update student
        - [ ] csv upload bulk
        - [ ] student list (show, sort, search)
        - [ ] download student list (general, by parent/child class, solo)
    - [ ] school staff menu (admin, registrar)
        - [ ] add/update staff
        - [ ] csv upload bulk
        - [ ] download staff list
        - [ ] staff list (show, sort, search)
    - [ ] invoice menu (admin, accountant)
        - [ ] add/update invoice (general, by parent/child class, solo)
        - [ ] add/update invoice payment
        - [ ] csv upload bulk
        - [ ] download invoice list (general, by parent/child class, solo)
        - [ ] invoice list (show, sort, search)
    - [ ] note menu (admin, lecturer)
        - [ ] add/update note
        - [ ] csv upload bulk
        - [ ] note list (show, sort, search)
        - [ ] results
            - [ ] by session, parent/child class
            - [ ] by session, term, parent/child class
    - [ ] extras menu (admin)
        - [x] add/update session
        - [x] add/update term
        - [x] add/update course
        - [x] add/update class
            - [x] parent class
            - [x] child class
    - [ ] tools (admin)
        - [ ] import data
        - [ ] export data
    - [ ] FAQ
    - [ ] License
    - [ ] Translation (English and French)
- [ ] back-end
    - [x] config the debug log
    - [ ] core
        - [ ] user info
        - [ ] system config (session, term, parent/child class)
    - [ ] student
        - [ ] info
    - [ ] school staff
        - [ ] info
    - [ ] invoice
        - [ ] invoice (school fees 50,000)
        - [ ] invoice transaction (10,000+25,000+15,000=50,000)
    - [ ] note
        - [ ] note
    - [ ] refactor (eg: templates/session, ...)
    - [ ] review the string representation of the models
