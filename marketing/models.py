from django.db import models


class FAQ(models.Model):

    question = models.CharField(default="", max_length=100)

    answer = models.CharField(default="", max_length=500)

    order = models.IntegerField(default=10, help_text="The index order to place.")

    class Meta:
        db_table = "faq_tbl"
        ordering = ["order"]
        verbose_name = "FAQ"
        verbose_name_plural = "FAQs"

    def __str__(self):
        return self.short_q

    @property
    def short_q(self):
        if len(self.question) >= 22:
            return self.question[:22] + "..."
        return self.question

    @property
    def short_a(self):
        if len(self.answer) >= 22:
            return self.answer[:22] + "..."
        return self.answer
