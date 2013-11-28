#=== Cliente ===================================================================================
def clientes(request):
    clientes = Cliente.objects.all()
    context = {'clientes': clientes, }
    return render(request, 'cliente.html', context)


def cliente(request, pk=0):
    if request.method == 'POST':
        return cliente_save(request, pk)
    else:
        if int(pk) == 0:
            return cliente_add(request)
        else:
            return cliente_edit(request, pk)


def cliente_add(request):
    form = ClienteForm()
    context = {'form': form, }
    return render(request, 'cliente.html', context)


def cliente_edit(request, pk):
    cliente = get_object_or_404(Cliente, pk=pk)
    form = ClienteForm(instance=cliente)
    context = {'form': form}
    return render(request, 'cliente.html', context)


def cliente_save(request, pk):
    form = ClienteForm(request.POST)
    if not form.is_valid():
        return render(request, 'cliente.html', {'form': form, })

    if int(pk) > 0:
        cliente = form.save(commit=False)
        cliente.id = pk

    form.save()
    return HttpResponseRedirect(reverse('cliente_list'))


def cliente_delete(request, pk):
    cliente = get_object_or_404(Cliente, pk=pk)
    if request.GET.get('confirm') == 'ok':
        cliente.delete()
        return HttpResponseRedirect(reverse('cliente_list'))
    else:
        context = {'model_name': 'Cliente',
                   'model': cliente,
                   'url_confirm': reverse('cliente_delete', args=[cliente.pk]),
                   'url_cancel': reverse('cliente_list'),
        }
        return render(request, 'base_delete.html', context)

#=== Cliente =================================================================================== 