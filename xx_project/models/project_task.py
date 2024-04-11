from odoo import fields, api, models, _
import ast


class Task(models.Model):
    _inherit = "project.task"

    def action_view_project_tasks(self):
        """
        Action to open the task overview in kanban view
        """
        action = self.env['ir.actions.act_window'].with_context({'active_id': self.project_id.id})._for_xml_id('project.act_project_project_2_project_task_all')
        action['display_name'] = _("%(name)s", name=self.project_id.name)
        context = action['context'].replace('active_id', str(self.project_id.id))
        context = ast.literal_eval(context)
        context.update({
            'create': self.active,
            'active_test': self.active
            })
        action['context'] = context
        return action
