# Desenvolvimento de Aplicações em Python

Repositório com os exercícios e projetos da matéria **Desenvolvimento de Aplicações em Python**, voltada ao desenvolvimento rápido de aplicações (RAD).

## Conteúdo

| Pasta | Assunto |
|-------|---------|
| [Tkinter](Tkinter/) | Interfaces gráficas desktop com Tkinter |

### Tkinter

Exemplos didáticos, todos orientados a objetos (uma classe por aplicação):

| Arquivo | O que demonstra |
|---------|-----------------|
| `helloapp.py` | Label, campo de texto com texto-guia (placeholder) e botão que exibe um olá |
| `focoapp.py` | Eventos de foco (`FocusIn` / `FocusOut`) para limpar e restaurar o placeholder |
| `eventoapp.py` | Evento de clique em botão (`ttk.Button`) alterando um label |
| `menuapp.py` | Barra de menus (Arquivo / Ajuda), `messagebox` e janela secundária (`Toplevel`) |
| `gradeapp.py` | Gerenciador `grid` e o parâmetro `sticky` |
| `grid_responsivo_app.py` | Grid responsivo com `columnconfigure` / `rowconfigure` (`weight` e `minsize`) |

## Como executar

Requer Python 3 (o Tkinter já vem incluído).

```bash
python Tkinter/helloapp.py
```

> Novos conteúdos da matéria serão adicionados ao longo do semestre.
