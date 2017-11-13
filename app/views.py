from flask import render_template
from flask.ext.appbuilder.models.sqla.interface import SQLAInterface
from flask.ext.appbuilder import ModelView
from app import appbuilder, db

from flask import render_template
from flask_appbuilder import BaseView, expose, has_access
from app import appbuilder

class MyView(BaseView):

    default_view = 'method1'

    @expose('/method1/')
    @has_access
    def method1(self):
            # do something with param1
            # and return to previous page or index
        return self.render_template('accordion.html')

    @expose('/method2/<string:param1>')
    @has_access
    def method2(self, param1):
        # do something with param1
        # and render template with param
        param1 = 'Goodbye %s' % (param1)
        return param1

    @expose('/method3/')
    @has_access
    def method3(self):
        # do something with param1
        # and render template with param

        return self.render_template('accordion.html')


appbuilder.add_view(MyView(), "Method1", category='My View')
#appbuilder.add_view(MyView(), "Method2", href='/myview/method2/jonh', category='My View')
# Use add link instead there is no need to create MyView twice.
appbuilder.add_link("Method2", href='/myview/method2/jonh', category='My View')
appbuilder.add_link(MyView(), "Method3", category='My View')

"""
    Application wide 404 error handler
"""
@appbuilder.app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html', base_template=appbuilder.base_template, appbuilder=appbuilder), 404

db.create_all()


