# cowsay_draw.py
import cowsay

# Criando um desenho personalizado
desenho_personalizado = r"""
     \   ^__^
      \  (oo)\_______
         (__)\       )\/\
             ||----w |
             ||     ||
"""

# Usando a função .draw() com o desenho personalizado
cowsay.draw(desenho_personalizado, "Olá! Este é meu desenho personalizado!")

# Outro exemplo com um desenho mais simples
desenho_simples = r"""
  -----
 / Hello \
 \ World /
  -----
     \
      \
        ^__^
        (oo)\_______
        (__)\       )\/\
            ||----w |
            ||     ||
"""

cowsay.draw(desenho_simples, "Programando com Python é divertido!")