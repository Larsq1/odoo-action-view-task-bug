from odoo import fields, api, models


class Task(models.Model):
    _inherit = "project.task"

    def action_view_project_tasks(self):
        """
        Action to open the task overview in kanban view
        """
        action = self.project_id.with_context(active_id=self.project_id.id, active_ids=self.project_id.ids,
                                              active_model=self.project_id._name).action_view_tasks()
        return action
