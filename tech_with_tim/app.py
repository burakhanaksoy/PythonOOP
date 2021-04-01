from public_vs_private_classes import NotPrivate, _Private

foo = NotPrivate('foo')
foo.display()
foo._display()

bar = _Private('Bar')
bar._show()
# Actually, the word 'private' is just telling someone or yourself that
# that class, var, or method is private and shouldn't be tempered / messed with..
# As you can see, we can reach private classes and variables easily,
# so it's just an 'idea' rather than 'restriction', unlike Java