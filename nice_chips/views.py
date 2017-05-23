# imports
from . forms import DraftForm, ReminderForm
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.http import HttpResponseRedirect, Http404
from django.views import View
from django.views.generic.edit import CreateView
from django.views.generic.list import ListView
from django.contrib.auth.mixins import LoginRequiredMixin


from . models import Draft, Reminder



# class views for index draft
class IndexDraftView(View):
    template_name = 'nice_chips/draft/index_draft.html'

    def get(self, request):
        title = 'Мой черновик'
        draft = Draft.objects.filter(drafts=request.user).order_by('-date_added')
        return render(request, self.template_name, {'title': title, 'draft': draft})


# class views for index draft
class IndexReminderView(LoginRequiredMixin, ListView):
    context_object_name = 'reminder'
    queryset = Draft.objects.filter(reminders=request.user).order_by('-date_added')
    template_name = 'nice_chips/reminder/index_reminder.html'



# views for add my draft
class DraftAddView(LoginRequiredMixin, CreateView):
    model = Draft
    form_class = DraftForm
    template_name = 'nice_chips/draft/add_draft.html'
    success_url = '/nice_chips/index_draft/'

    def form_valid(self, form):
        form.instance.drafts = self.request.user
        return super(DraftAddView, self).form_valid(form)


class ReminderAddView(CreateView):
    model = Reminder
    form_class = ReminderForm
    template_name = 'nice_chips/reminder/add_reminder.html'
    success_url = '/nice_chips/index_reminder/'

    def form_valid(self, form):
        form.instance.reminders = self.request.user
        return super(ReminderAddView, self).form_valid(form)






# views for edit my draft
@login_required()
def edit_draft(request, draft_id):
    title = 'Редактирование записи в черновике'
    draft = Draft.objects.get(id=draft_id)

    if draft.drafts != request.user:
        raise Http404

    if request.method != 'POST':
        form = DraftForm(instance=draft)

    else:
        form = DraftForm(data=request.POST, instance=draft)

        if form.is_valid():
            new_draft = form.save(commit=False)
            new_draft.drafts = request.user
            new_draft.save()
            return HttpResponseRedirect(reverse('nice_chips:index_draft'))

    context = {'title': title, 'draft': draft, 'form': form}
    return render(request, 'nice_chips/draft/edit_draft.html', context)




# views for delete draft
@login_required()
def delete_draft(request, draft_id):
    draft = Draft.objects.get(id=draft_id)

    if draft.drafts != request.user:
        raise Http404

    draft.delete()
    return HttpResponseRedirect(reverse('nice_chips:index_draft'))



