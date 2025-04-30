import json
import os
from time import sleep
from datetime import datetime
import re

arquivo = 'alunos.json'
espace = '\033[1;35m=\033[0m' * 89
titulo = '\033[1;36m CLICKEDU  \033[0m'
print(espace)
print(titulo.center(100, ' '))
print(espace)

quest_seg12 = [
    {
        "pergunta": "\033[35m1\033[0m""\033[36m Qual das opções não faz parte dos princípios da segurança digital?\033[0m",
        "opcoes": {
            "\033[35ma\033[0m": "\033[36mAutenticidade\033[0m",
            "\033[35mb\033[0m": "\033[36mConfidencialidade\033[0m",
            "\033[35mc\033[0m": "\033[36mIntegridade\033[0m",
            "\033[35md\033[0m": "\033[36mDisponibilidade\033[0m",
        },
        "resposta_correta": "a"
    },
    {
        "pergunta": "\033[35m2\033[0m""\033[36m Qual dessas ameaças é um tipo de software malicioso que sequestra seus dados e exige pagamento?\033[0m",
        "opcoes": {
            "\033[35ma\033[0m": "\033[36mVírus\033[0m",
            "\033[35mb\033[0m": "\033[36mSpyware\033[0m",
            "\033[35mc\033[0m": "\033[36mRansomware\033[0m",
            "\033[35md\033[0m": "\033[36mPhishing\033[0m",
        },
        "resposta_correta": "c"
    },
    {
        "pergunta": "\033[35m3\033[0m""\033[36m O que caracteriza um ataque de engenharia social?\033[0m",
        "opcoes": {
            "\033[35ma\033[0m": "\033[36mUso de senhas fracas\033[0m",
            "\033[35mb\033[0m": "\033[36mManipulação de pessoas para obter informações\033[0m",
            "\033[35mc\033[0m": "\033[36mInvasão de sistemas por força bruta\033[0m",
            "\033[35md\033[0m": "\033[36mEspalhamento de vírus por redes sociais\033[0m",
        },
        "resposta_correta": "b"
    },
    {
        "pergunta": "\033[35m4\033[0m""\033[36m O que é phishing?\033[0m",
        "opcoes": {
            "\033[35ma\033[0m": "\033[36mUm ataque que impede o acesso ao sistema\033[0m",
            "\033[35mb\033[0m": "\033[36mUm software que rouba senhas por força bruta\033[0m",
            "\033[35mc\033[0m": "\033[36mUma técnica para enganar pessoas e obter dados pessoais\033[0m",
            "\033[35md\033[0m": "\033[36mUm programa que protege contra vírus\033[0m",
        },
        "resposta_correta": "c"
    },
    {
        "pergunta": "\033[35m5\033[0m""\033[36m Qual das opções abaixo é uma consequência da falta de segurança digital?\033[0m",
        "opcoes": {
            "\033[35ma\033[0m": "\033[36mAumento da velocidade da internet\033[0m",
            "\033[35mb\033[0m": "\033[36mMelhora na experiência do usuário\033[0m",
            "\033[35mc\033[0m": "\033[36mRedução do consumo de bateria\033[0m",
            "\033[35md\033[0m": "\033[36mRoubo de identidade e fraudes\033[0m",
        },
        "resposta_correta": "d"
    },
    {
        "pergunta": "\033[35m6\033[0m""\033[36m O que garante a confidencialidade da informação?\033[0m",
        "opcoes": {
            "\033[35ma\033[0m": "\033[36mQue os dados sejam acessíveis a qualquer momento\033[0m",
            "\033[35mb\033[0m": "\033[36mQue apenas pessoas autorizadas tenham acesso\033[0m",
            "\033[35mc\033[0m": "\033[36mQue o sistema funcione corretamente\033[0m",
            "\033[35md\033[0m": "\033[36mQue os dados possam ser alterados por qualquer pessoa\033[0m",
        },
        "resposta_correta": "b"
    },
    {
        "pergunta": "\033[35m7\033[0m""\033[36m Por que a segurança digital é importante para instituições como hospitais e escolas?\033[0m",
        "opcoes": {
            "\033[35ma\033[0m": "\033[36mPara reduzir custos operacionais\033[0m",
            "\033[35mb\033[0m": "\033[36mPara aumentar a visibilidade online\033[0m",
            "\033[35mc\033[0m": "\033[36mPara garantir o funcionamento seguro e a proteção de dados sensíveis\033[0m",
            "\033[35md\033[0m": "\033[36mPara facilitar o acesso de qualquer pessoa aos dados\033[0m",
        },
        "resposta_correta": "c"
    },
    {
        "pergunta": "\033[35m8\033[0m""\033[36m O que é spyware?\033[0m",
        "opcoes": {
            "\033[35ma\033[0m": "\033[36mUm antivírus gratuito\033[0m",
            "\033[35mb\033[0m": "\033[36mUm programa que remove vírus do sistema\033[0m",
            "\033[35mc\033[0m": "\033[36mUm sistema de backup\033[0m",
            "\033[35md\033[0m": "\033[36mUm software que espiona atividades para roubar dados\033[0m",
        },
        "resposta_correta": "d"
    },
    {
        "pergunta": "\033[35m9\033[0m""\033[36m A LGPD (Lei Geral de Proteção de Dados) serve para:\033[0m",
        "opcoes": {
            "\033[35ma\033[0m": "\033[36mRegular a coleta e uso de dados pessoais com responsabilidade\033[0m",
            "\033[35mb\033[0m": "\033[36mPromover o livre acesso à internet\033[0m",
            "\033[35mc\033[0m": "\033[36mGarantir que empresas possam vender dados\033[0m",
            "\033[35md\033[0m": "\033[36mBloquear totalmente o uso de dados na internet\033[0m",
        },
        "resposta_correta": "a"
    },
    {
        "pergunta": "\033[35m10\033[0m""\033[36m Qual destas frases está correta?\033[0m",
        "opcoes": {
            "\033[35ma\033[0m": "\033[36mA segurança digital é um problema apenas das empresas.\033[0m",
            "\033[35mb\033[0m": "\033[36mTer segurança digital ajuda a proteger outras pessoas também.\033[0m",
            "\033[35mc\033[0m": "\033[36mOs antivírus tornam a segurança digital desnecessária.\033[0m",
            "\033[35md\033[0m": "\033[36mA internet é 100% segura, por isso não é preciso se preocupar\033[0m",
        },
        "resposta_correta": "b"
    }
]

quest_seg_34 = [
    {
        "pergunta": "\033[35m1\033[0m""\033[36m Qual dos itens abaixo não é um tipo de malware?\033[0m",
        "opcoes": {
            "\033[35ma\033[0m": "\033[36mSpyware\033[0m",
            "\033[35mb\033[0m": "\033[36mAdware\033[0m",
            "\033[35mc\033[0m": "\033[36mRansomware\033[0m",
            "\033[35md\033[0m": "\033[36mFirewall\033[0m"
        },
        "resposta_correta": "d"
    },
    {
        "pergunta": "\033[35m2\033[0m""\033[36m O que caracteriza um ataque DDoS?\033[0m",
        "opcoes": {
            "\033[35ma\033[0m": "\033[36mEspionar atividades do usuário\033[0m",
            "\033[35mb\033[0m": "\033[36mFazer o sistema sair do ar por excesso de acessos falsos\033[0m",
            "\033[35mc\033[0m": "\033[36mRoubar dados por meio de engenharia social\033[0m",
            "\033[35md\033[0m": "\033[36mInvadir contas bancárias com senhas fracas\033[0m"
        },
        "resposta_correta": "b"
    },
    {
        "pergunta": "\033[35m3\033[0m""\033[36m Qual dessas opções é um exemplo clássico de phishing?\033[0m",
        "opcoes": {
            "\033[35ma\033[0m": "\033[36mUma notificação real de atualização do seu navegador\033[0m",
            "\033[35mb\033[0m": "\033[36mUm antivírus detectando uma ameaça\033[0m",
            "\033[35mc\033[0m": "\033[36mUm backup automático feito pelo sistema\033[0m",
            "\033[35md\033[0m": "\033[36mUm link enviado por SMS dizendo que sua conta foi bloqueada e pedindo verificação de dados\033[0m"
        },
        "resposta_correta": "d"
    },
    {
        "pergunta": "\033[35m4\033[0m""\033[36m O que é engenharia social?\033[0m",
        "opcoes": {
            "\033[35ma\033[0m": "\033[36mUm ataque ao hardware do computador\033[0m",
            "\033[35mb\033[0m": "\033[36mUm sistema de criptografia de dados\033[0m",
            "\033[35mc\033[0m": "\033[36mUma forma de manipular pessoas para obter informações\033[0m",
            "\033[35md\033[0m": "\033[36mUm antivírus mal configurado\033[0m"
        },
        "resposta_correta": "c"
    },
    {
        "pergunta": "\033[35m5\033[0m""\033[36m O que é essencial para uma senha forte?\033[0m",
        "opcoes": {
            "\033[35ma\033[0m": "\033[36mTer letras, números, símbolos e ser única para cada conta\033[0m",
            "\033[35mb\033[0m": "\033[36mUsar o nome da empresa e a data de nascimento\033[0m",
            "\033[35mc\033[0m": "\033[36mTer pelo menos 4 caracteres e ser fácil de lembrar\033[0m",
            "\033[35md\033[0m": "\033[36mSer usada em várias plataformas para facilitar o acesso\033[0m"
        },
        "resposta_correta": "a"
    },
    {
        "pergunta": "\033[35m6\033[0m""\033[36m A autenticação multifator (MFA) é importante porque:\033[0m",
        "opcoes": {
            "\033[35ma\033[0m": "\033[36mSubstitui completamente a senha\033[0m",
            "\033[35mb\033[0m": "\033[36mAdiciona uma segunda verificação além da senha\033[0m",
            "\033[35mc\033[0m": "\033[36mProtege seus dados contra o backup automático\033[0m",
            "\033[35md\033[0m": "\033[36mAumenta a velocidade de conexão da internet\033[0m"
        },
        "resposta_correta": "b"
    },
    {
        "pergunta": "\033[35m7\033[0m""\033[36m O que você deve evitar ao usar Wi-Fi público?\033[0m",
        "opcoes": {
            "\033[35ma\033[0m": "\033[36mFazer transações bancárias ou acessar e-mails importantes\033[0m",
            "\033[35mb\033[0m": "\033[36mAssistir vídeos em streaming\033[0m",
            "\033[35mc\033[0m": "\033[36mAcessar redes sociais\033[0m",
            "\033[35md\033[0m": "\033[36mUsar VPN\033[0m"
        },
        "resposta_correta": "a"
    },
    {
        "pergunta": "\033[35m8\033[0m""\033[36m Por que manter o sistema atualizado é importante para a segurança?\033[0m",
        "opcoes": {
            "\033[35ma\033[0m": "\033[36mPara economizar espaço no dispositivo\033[0m",
            "\033[35mb\033[0m": "\033[36mPara desbloquear mais jogos e aplicativos\033[0m",
            "\033[35mc\033[0m": "\033[36mPorque corrige falhas que podem ser exploradas por hackers\033[0m",
            "\033[35md\033[0m": "\033[36mPorque melhora a conexão com a internet\033[0m"
        },
        "resposta_correta": "c"
    },
    {
        "pergunta": "\033[35m9\033[0m""\033[36m O que o cadeado na barra de endereço de um site indica?\033[0m",
        "opcoes": {
            "\033[35ma\033[0m": "\033[36mO site está fora do ar\033[0m",
            "\033[35mb\033[0m": "\033[36mA conexão é segura (uso de HTTPS)\033[0m",
            "\033[35mc\033[0m": "\033[36mO conteúdo está bloqueado\033[0m",
            "\033[35md\033[0m": "\033[36mO site tem anúncios protegidos\033[0m"
        },
        "resposta_correta": "b"
    },
    {
        "pergunta": "\033[35m10\033[0m""\033[36m Qual das práticas abaixo ajuda a minimizar a perda de dados em caso de ataque?\033[0m",
        "opcoes": {
            "\033[35ma\033[0m": "\033[36mFazer backups regulares e manter cópias offline\033[0m",
            "\033[35mb\033[0m": "\033[36mUsar antivírus gratuito\033[0m",
            "\033[35mc\033[0m": "\033[36mCompartilhar senhas com colegas de confiança\033[0m",
            "\033[35md\033[0m": "\033[36mDeixar o firewall desativado para facilitar o acesso\033[0m"
        },
        "resposta_correta": "a"
    }
]

quest_pens_12 = [ # questionario do modulo de pensamento do 01 ao 02
    {
        "pergunta": "\033[35m1\033[0m \033[36mO que é pensamento computacional?\033[0m",
        "opcoes": {
            "\033[35ma\033[0m": "\033[36mProgramar sistemas de computador\033[0m",
            "\033[35mb\033[0m": "\033[36mResolver problemas de forma emocional\033[0m",
            "\033[35mc\033[0m": "\033[36mResolver problemas de maneira lógica, sistemática e eficiente\033[0m",
            "\033[35md\033[0m": "\033[36mUsar computadores para tarefas cotidianas\033[0m"
        },
        "resposta_correta": "c"
    },
    {
        "pergunta": "\033[35m2\033[0m \033[36mQual das opções representa a habilidade de decomposição?\033[0m",
        "opcoes": {
            "\033[35ma\033[0m": "\033[36mFazer uma pergunta sobre o problema\033[0m",
            "\033[35mb\033[0m": "\033[36mDividir um problema em partes menores e mais simples\033[0m",
            "\033[35mc\033[0m": "\033[36mIgnorar detalhes do problema\033[0m",
            "\033[35md\033[0m": "\033[36mCriar gráficos sobre o problema\033[0m"
        },
        "resposta_correta": "b"
    },
    {
        "pergunta": "\033[35m3\033[0m \033[36mUm exemplo de abstração é:\033[0m",
        "opcoes": {
            "\033[35ma\033[0m": "\033[36mIgnorar o processo de preparo da comida ao pedir por aplicativo\033[0m",
            "\033[35mb\033[0m": "\033[36mSeparar o orçamento da viagem por categoria\033[0m",
            "\033[35mc\033[0m": "\033[36mSeguir uma receita de bolo\033[0m",
            "\033[35md\033[0m": "\033[36mComparar preços em diferentes sites\033[0m"
        },
        "resposta_correta": "a"
    },
    {
        "pergunta": "\033[35m4\033[0m \033[36mQual habilidade do pensamento computacional envolve encontrar repetições ou tendências?\033[0m",
        "opcoes": {
            "\033[35ma\033[0m": "\033[36mDecomposição\033[0m",
            "\033[35mb\033[0m": "\033[36mAlgoritmos\033[0m",
            "\033[35mc\033[0m": "\033[36mReconhecimento de padrões\033[0m",
            "\033[35md\033[0m": "\033[36mAbstração\033[0m"
        },
        "resposta_correta": "c"
    },
    {
        "pergunta": "\033[35m5\033[0m \033[36mO que é um algoritmo?\033[0m",
        "opcoes": {
            "\033[35ma\033[0m": "\033[36mUma linguagem de programação\033[0m",
            "\033[35mb\033[0m": "\033[36mUma ordem de comandos aleatórios\033[0m",
            "\033[35mc\033[0m": "\033[36mUm tipo de vírus digital\033[0m",
            "\033[35md\033[0m": "\033[36mUma sequência de passos para resolver um problema\033[0m"
        },
        "resposta_correta": "d"
    },
    {
        "pergunta": "\033[35m6\033[0m \033[36mQual destas afirmações é uma proposição?\033[0m",
        "opcoes": {
            "\033[35ma\033[0m": "\033[36mO sol nasce no leste.\033[0m",
            "\033[35mb\033[0m": "\033[36mComo vai você?\033[0m",
            "\033[35mc\033[0m": "\033[36mFeche a porta!\033[0m",
            "\033[35md\033[0m": "\033[36mVamos sair hoje?\033[0m"
        },
        "resposta_correta": "a"
    },
    {
        "pergunta": "\033[35m7\033[0m \033[36mQual destas frases não é uma proposição?\033[0m",
        "opcoes": {
            "\033[35ma\033[0m": "\033[36mA água ferve a 100°C.\033[0m",
            "\033[35mb\033[0m": "\033[36m1 + 1 = 3.\033[0m",
            "\033[35mc\033[0m": "\033[36mEstude bastante!\033[0m",
            "\033[35md\033[0m": "\033[36mA Terra é redonda.\033[0m"
        },
        "resposta_correta": "c"
    },
    {
        "pergunta": "\033[35m8\033[0m \033[36mA lógica computacional funciona com base em:\033[0m",
        "opcoes": {
            "\033[35ma\033[0m": "\033[36mEmoções humanas\033[0m",
            "\033[35mb\033[0m": "\033[36mIntuição e criatividade\033[0m",
            "\033[35mc\033[0m": "\033[36mProvas matemáticas complexas\033[0m",
            "\033[35md\033[0m": "\033[36mValores Verdadeiro (1) e Falso (0)\033[0m"
        },
        "resposta_correta": "d"
    },
    {
        "pergunta": "\033[35m9\033[0m \033[36mEm lógica verbal, qual dedução está correta?\033[0m",
        "opcoes": {
            "\033[35ma\033[0m": "\033[36mSe todos os cães latem e Rex mia, então Rex é cão.\033[0m",
            "\033[35mb\033[0m": "\033[36mSe todo peixe nada e Nemo nada, então Nemo é peixe.\033[0m",
            "\033[35mc\033[0m": "\033[36mSe todas as flores têm cheiro e a rosa não tem, então rosa não é flor.\033[0m",
            "\033[35md\033[0m": "\033[36mSe todo pássaro voa e o avião voa, então avião é pássaro.\033[0m"
        },
        "resposta_correta": "b"
    },
    {
        "pergunta": "\033[35m10\033[0m \033[36mEm uma sequência numérica: 2, 4, 6, ___, ___ — os dois próximos números são:\033[0m",
        "opcoes": {
            "\033[35ma\033[0m": "\033[36m8 e 9\033[0m",
            "\033[35mb\033[0m": "\033[36m7 e 9\033[0m",
            "\033[35mc\033[0m": "\033[36m8 e 10\033[0m",
            "\033[35md\033[0m": "\033[36m10 e 12\033[0m"
        },
        "resposta_correta": "c"
    }
]

quest_pens_34 = [ #questionario do modulo pensamento do 3 ao 4
        {
            "pergunta": "\033[35m1\033[0m \033[36mO que define um algoritmo?\033[0m",
            "opcoes": {
                "\033[35ma\033[0m": "\033[36mUm código escrito em linguagem de máquina\033[0m",
                "\033[35mb\033[0m": "\033[36mUm conjunto de imagens digitais\033[0m",
                "\033[35mc\033[0m": "\033[36mUm programa pronto que roda automaticamente\033[0m",
                "\033[35md\033[0m": "\033[36mUma sequência lógica e finita de passos para resolver um problema\033[0m"
            },
            "resposta_correta": "d"
        },
        {
            "pergunta": "\033[35m2\033[0m \033[36mQual das opções representa corretamente os componentes básicos de um algoritmo?\033[0m",
            "opcoes": {
                "\033[35ma\033[0m": "\033[36mEntrada, processamento e saída\033[0m",
                "\033[35mb\033[0m": "\033[36mEntrada, comando e repetição\033[0m",
                "\033[35mc\033[0m": "\033[36mPergunta, resposta e verificação\033[0m",
                "\033[35md\033[0m": "\033[36mNúmero, texto e cálculo\033[0m"
            },
            "resposta_correta": "a"
        },
        {
            "pergunta": "\033[35m3\033[0m \033[36mO que é considerado uma boa característica de um algoritmo?\033[0m",
            "opcoes": {
                "\033[35ma\033[0m": "\033[36mSer curto e enigmático\033[0m",
                "\033[35mb\033[0m": "\033[36mSer executado apenas por profissionais\033[0m",
                "\033[35mc\033[0m": "\033[36mSer claro, objetivo e executável\033[0m",
                "\033[35md\033[0m": "\033[36mUsar termos técnicos difíceis\033[0m"
            },
            "resposta_correta": "c"
        },
        {
            "pergunta": "\033[35m4\033[0m \033[36mQual das opções abaixo mostra um exemplo de entrada em um algoritmo?\033[0m",
            "opcoes": {
                "\033[35ma\033[0m": "\033[36mCalcular a média de duas notas\033[0m",
                "\033[35mb\033[0m": "\033[36mExibir o resultado final\033[0m",
                "\033[35mc\033[0m": "\033[36mInformar as duas notas\033[0m",
                "\033[35md\033[0m": "\033[36mMostrar se o aluno passou ou não\033[0m"
            },
            "resposta_correta": "c"
        },
        {
            "pergunta": "\033[35m5\033[0m \033[36mPor que representar um algoritmo de forma estruturada é importante?\033[0m",
            "opcoes": {
                "\033[35ma\033[0m": "\033[36mTorna mais difícil copiar a ideia\033[0m",
                "\033[35mb\033[0m": "\033[36mAjuda a manter o algoritmo secreto\033[0m",
                "\033[35mc\033[0m": "\033[36mFacilita a visualização, comunicação e identificação de erros\033[0m",
                "\033[35md\033[0m": "\033[36mServe apenas para programadores profissionais\033[0m"
            },
            "resposta_correta": "c"
        },
        {
            "pergunta": "\033[35m6\033[0m \033[36mA representação de algoritmo em forma de narrativa se caracteriza por:\033[0m",
            "opcoes": {
                "\033[35ma\033[0m": "\033[36mUsar códigos e símbolos gráficos\033[0m",
                "\033[35mb\033[0m": "\033[36mUsar linguagem natural para descrever as etapas\033[0m",
                "\033[35mc\033[0m": "\033[36mSer escrita em inglês técnico\033[0m",
                "\033[35md\033[0m": "\033[36mExigir conhecimentos de programação\033[0m"
            },
            "resposta_correta": "b"
        },
        {
            "pergunta": "\033[35m7\033[0m \033[36mQual símbolo em um fluxograma representa uma decisão (como “sim ou não”)?\033[0m",
            "opcoes": {
                "\033[35ma\033[0m": "\033[36mElipse\033[0m",
                "\033[35mb\033[0m": "\033[36mRetângulo\033[0m",
                "\033[35mc\033[0m": "\033[36mCírculo\033[0m",
                "\033[35md\033[0m": "\033[36mLosango\033[0m"
            },
            "resposta_correta": "d"
        },
        {
            "pergunta": "\033[35m8\033[0m \033[36mO que é pseudocódigo?\033[0m",
            "opcoes": {
                "\033[35ma\033[0m": "\033[36mUma forma de escrever algoritmos parecida com programação, mas em linguagem natural estruturada\033[0m",
                "\033[35mb\033[0m": "\033[36mUm código secreto para proteger dados\033[0m",
                "\033[35mc\033[0m": "\033[36mUm fluxograma simplificado com imagens\033[0m",
                "\033[35md\033[0m": "\033[36mUma forma de traduzir textos automaticamente\033[0m"
            },
            "resposta_correta": "a"
        },
        {
            "pergunta": "\033[35m9\033[0m \033[36mQuando é mais adequado usar a representação visual (fluxograma)?\033[0m",
            "opcoes": {
                "\033[35ma\033[0m": "\033[36mQuando se deseja decorar um algoritmo\033[0m",
                "\033[35mb\033[0m": "\033[36mPara entender decisões e fluxo de processos\033[0m",
                "\033[35mc\033[0m": "\033[36mPara copiar algoritmos prontos\033[0m",
                "\033[35md\033[0m": "\033[36mApenas em provas técnicas\033[0m"
            },
            "resposta_correta": "b"
        },
        {
            "pergunta": "\033[35m10\033[0m \033[36mComparando as representações de algoritmos, qual delas mais aproxima da lógica de programação real?\033[0m",
            "opcoes": {
                "\033[35ma\033[0m": "\033[36mPseudocódigo\033[0m",
                "\033[35mb\033[0m": "\033[36mNarrativa\033[0m",
                "\033[35mc\033[0m": "\033[36mFluxograma\033[0m",
                "\033[35md\033[0m": "\033[36mLinguagem matemática\033[0m"
            },
            "resposta_correta": "a"
        }
    ]

quest_python_1234 = [
    {
        "pergunta": "\033[35m1\033[0m \033[36mQual é a principal função de uma variável em Python?\033[0m",
        "opcoes": {
            "\033[35ma\033[0m": "\033[36mCriar gráficos\033[0m",
            "\033[35mb\033[0m": "\033[36mMostrar mensagens na tela\033[0m",
            "\033[35mc\033[0m": "\033[36mConverter dados em imagens\033[0m",
            "\033[35md\033[0m": "\033[36mArmazenar valores na memória\033[0m"
        },
        "resposta_correta": "d"
    },
    {
        "pergunta": "\033[35m2\033[0m \033[36mQual tipo de dado é utilizado para guardar valores como 'Olá, mundo!'?\033[0m",
        "opcoes": {
            "\033[35ma\033[0m": "\033[36mint\033[0m",
            "\033[35mb\033[0m": "\033[36mfloat\033[0m",
            "\033[35mc\033[0m": "\033[36mstring\033[0m",
            "\033[35md\033[0m": "\033[36mbool\033[0m"
        },
        "resposta_correta": "c"
    },
    {
        "pergunta": "\033[35m3\033[0m \033[36mQual é o resultado da conversão: int('10')?\033[0m",
        "opcoes": {
            "\033[35ma\033[0m": "\033[36m'10'\033[0m",
            "\033[35mb\033[0m": "\033[36m10\033[0m",
            "\033[35mc\033[0m": "\033[36m10.0\033[0m",
            "\033[35md\033[0m": "\033[36mErro\033[0m"
        },
        "resposta_correta": "b"
    },
    {
        "pergunta": "\033[35m4\033[0m \033[36mO que o valor False representa em Python?\033[0m",
        "opcoes": {
            "\033[35ma\033[0m": "\033[36mUm valor lógico falso\033[0m",
            "\033[35mb\033[0m": "\033[36mUm número\033[0m",
            "\033[35mc\033[0m": "\033[36mUm texto\033[0m",
            "\033[35md\033[0m": "\033[36mUm erro de código\033[0m"
        },
        "resposta_correta": "a"
    },
    {
        "pergunta": "\033[35m5\033[0m \033[36mDado altura = 1.75, o que int(altura) retornará?\033[0m",
        "opcoes": {
            "\033[35ma\033[0m": "\033[36m1.75\033[0m",
            "\033[35mb\033[0m": "\033[36m2\033[0m",
            "\033[35mc\033[0m": "\033[36m1\033[0m",
            "\033[35md\033[0m": "\033[36m1.0\033[0m"
        },
        "resposta_correta": "c"
    },
    {
        "pergunta": "\033[35m6\033[0m \033[36mQual operador em Python é usado para obter o resto de uma divisão?\033[0m",
        "opcoes": {
            "\033[35ma\033[0m": "\033[36m%\033[0m",
            "\033[35mb\033[0m": "\033[36m//\033[0m",
            "\033[35mc\033[0m": "\033[36m**\033[0m",
            "\033[35md\033[0m": "\033[36m/\033[0m"
        },
        "resposta_correta": "a"
    },
    {
        "pergunta": "\033[35m7\033[0m \033[36mQual das expressões abaixo retorna True?\033[0m",
        "opcoes": {
            "\033[35ma\033[0m": "\033[36m5 < 3\033[0m",
            "\033[35mb\033[0m": "\033[36m7 == 8\033[0m",
            "\033[35mc\033[0m": "\033[36m4 != 4\033[0m",
            "\033[35md\033[0m": "\033[36m10 >= 5\033[0m"
        },
        "resposta_correta": "d"
    },
    {
        "pergunta": "\033[35m8\033[0m \033[36mO que a expressão not True retorna?\033[0m",
        "opcoes": {
            "\033[35ma\033[0m": "\033[36mTrue\033[0m",
            "\033[35mb\033[0m": "\033[36mErro\033[0m",
            "\033[35mc\033[0m": "\033[36mNone\033[0m",
            "\033[35md\033[0m": "\033[36mFalse\033[0m"
        },
        "resposta_correta": "d"
    },
    {
        "pergunta": "\033[35m9\033[0m \033[36mEm idade = 18 e tem_carteira = True, o que retorna idade >= 18 and tem_carteira?\033[0m",
        "opcoes": {
            "\033[35ma\033[0m": "\033[36mFalse\033[0m",
            "\033[35mb\033[0m": "\033[36mTrue\033[0m",
            "\033[35mc\033[0m": "\033[36mErro\033[0m",
            "\033[35md\033[0m": "\033[36mNone\033[0m"
        },
        "resposta_correta": "b"
    },
    {
        "pergunta": "\033[35m10\033[0m \033[36mQual função usamos para ler um valor digitado pelo usuário?\033[0m",
        "opcoes": {
            "\033[35ma\033[0m": "\033[36minput()\033[0m",
            "\033[35mb\033[0m": "\033[36mprint()\033[0m",
            "\033[35mc\033[0m": "\033[36mread()\033[0m",
            "\033[35md\033[0m": "\033[36mget()\033[0m"
        },
        "resposta_correta": "a"
    },
    {
        "pergunta": "\033[35m11\033[0m \033[36mQual das opções abaixo imprime corretamente: 'João tem 30 anos.' usando f-string?\033[0m",
        "opcoes": {
            "\033[35ma\033[0m": "\033[36mprint('João tem 30 anos.')\033[0m",
            "\033[35mb\033[0m": "\033[36mprint(f'João tem {30} anos.')\033[0m",
            "\033[35mc\033[0m": "\033[36mprint('João tem {} anos.'.format(30))\033[0m",
            "\033[35md\033[0m": "\033[36mprint(f'João tem {anos} anos.')\033[0m"
        },
        "resposta_correta": "b"
    },
    {
        "pergunta": "\033[35m12\033[0m \033[36mQual comando imprime um número com duas casas decimais?\033[0m",
        "opcoes": {
            "\033[35ma\033[0m": "\033[36mprint(numero)\033[0m",
            "\033[35mb\033[0m": "\033[36mprint(f'{numero}')\033[0m",
            "\033[35mc\033[0m": "\033[36mprint(f'{numero:.2f}')\033[0m",
            "\033[35md\033[0m": "\033[36mprint('{:.2f}'.format(numero))\033[0m"
        },
        "resposta_correta": "c"
    }
]

quest_python_5678 = [
    {
        "pergunta": "\033[35m1\033[0m \033[36mQual das alternativas representa corretamente uma estrutura de decisão com `if`, `elif` e `else`?\033[0m",
        "opcoes": {
            "\033[35ma\033[0m": "\033[36mif idade > 18:\nprint(\"Adulto\")\nelse idade == 18:\nprint(\"Dezoito anos\")\033[0m",
            "\033[35mb\033[0m": "\033[36mif idade > 18:\n    print(\"Adulto\")\nelif idade == 18:\n    print(\"Dezoito anos\")\nelse:\n    print(\"Menor de idade\")\033[0m",
            "\033[35mc\033[0m": "\033[36mif idade > 18\nprint(\"Adulto\")\nelif idade = 18\nprint(\"Dezoito anos\")\033[0m",
            "\033[35md\033[0m": "\033[36mif idade > 18:\nprint(\"Adulto\")\nelif: idade == 18\nprint(\"Dezoito anos\")\033[0m"
        },
        "resposta_correta": "b"
    },
    {
        "pergunta": "\033[35m2\033[0m \033[36mO que acontece no código abaixo?\n\nx = 0\nwhile x < 3:\n    print(x)\033[0m",
        "opcoes": {
            "\033[35ma\033[0m": "\033[36mEle imprime 0, 1, 2 e para.\033[0m",
            "\033[35mb\033[0m": "\033[36mEle gera erro porque o while está incorreto.\033[0m",
            "\033[35mc\033[0m": "\033[36mEle entra em loop infinito.\033[0m",
            "\033[35md\033[0m": "\033[36mEle imprime apenas o número 0.\033[0m"
        },
        "resposta_correta": "c"
    },
    {
        "pergunta": "\033[35m3\033[0m \033[36mQual é a principal diferença entre os laços `while` e `for` em Python?\033[0m",
        "opcoes": {
            "\033[35ma\033[0m": "\033[36mwhile só funciona com listas e for com números.\033[0m",
            "\033[35mb\033[0m": "\033[36mfor é usado quando a repetição depende de condição; while, quando sabemos quantas vezes repetir.\033[0m",
            "\033[35mc\033[0m": "\033[36mwhile é usado quando não sabemos o número exato de repetições; for é ideal quando sabemos.\033[0m",
            "\033[35md\033[0m": "\033[36mAmbos fazem a mesma coisa e não têm diferença.\033[0m"
        },
        "resposta_correta": "c"
    },
    {
        "pergunta": "\033[35m4\033[0m \033[36mO que o código a seguir imprime?\n\nfor i in range(2, 10, 3):\n    print(i)\033[0m",
        "opcoes": {
            "\033[35ma\033[0m": "\033[36m2 5 8\033[0m",
            "\033[35mb\033[0m": "\033[36m2 3 4 5 6 7 8 9\033[0m",
            "\033[35mc\033[0m": "\033[36m2 5 8 11\033[0m",
            "\033[35md\033[0m": "\033[36m2 6 10\033[0m"
        },
        "resposta_correta": "a"
    },
    {
        "pergunta": "\033[35m5\033[0m \033[36mQual dessas funções está corretamente definida e sendo chamada?\033[0m",
        "opcoes": {
            "\033[35ma\033[0m": "\033[36mdef somar(a, b):\n    return a + b\nprint(somar(2, 3))\033[0m",
            "\033[35mb\033[0m": "\033[36mdef somar(a, b):\n    print return a + b\nsomar(2, 3)\033[0m",
            "\033[35mc\033[0m": "\033[36mdef somar(a, b):\n    a + b\nprint(somar)\033[0m",
            "\033[35md\033[0m": "\033[36mdef somar(a, b)\n    return a + b\nprint(somar(2, 3))\033[0m"
        },
        "resposta_correta": "a"
    },
    {
        "pergunta": "\033[35m6\033[0m \033[36mQual alternativa **não** é uma função **built-in** do Python?\033[0m",
        "opcoes": {
            "\033[35ma\033[0m": "\033[36msum()\033[0m",
            "\033[35mb\033[0m": "\033[36mmax()\033[0m",
            "\033[35mc\033[0m": "\033[36mmostrar()\033[0m",
            "\033[35md\033[0m": "\033[36mlen()\033[0m"
        },
        "resposta_correta": "c"
    },
    {
        "pergunta": "\033[35m7\033[0m \033[36mQual a forma mais segura de abrir e ler um arquivo em Python, evitando esquecer de fechá-lo?\033[0m",
        "opcoes": {
            "\033[35ma\033[0m": "\033[36marquivo = open(\"texto.txt\", \"r\")\nprint(arquivo.read())\033[0m",
            "\033[35mb\033[0m": "\033[36marquivo = open(\"texto.txt\", \"r\")\nprint(arquivo.read())\narquivo.close()\033[0m",
            "\033[35mc\033[0m": "\033[36mwith open(\"texto.txt\", \"r\") as arquivo:\n    print(arquivo.read())\033[0m",
            "\033[35md\033[0m": "\033[36mprint(open(\"texto.txt\", \"r\"))\narquivo.close()\033[0m"
        },
        "resposta_correta": "c"
    },
    {
        "pergunta": "\033[35m8\033[0m \033[36mO que acontece se usarmos o modo \"w\" para abrir um arquivo com open()?\033[0m",
        "opcoes": {
            "\033[35ma\033[0m": "\033[36mO conteúdo será adicionado no final.\033[0m",
            "\033[35mb\033[0m": "\033[36mO conteúdo será mantido e atualizado linha por linha.\033[0m",
            "\033[35mc\033[0m": "\033[36mUm novo arquivo será criado apenas se ele não existir.\033[0m",
            "\033[35md\033[0m": "\033[36mO conteúdo antigo será apagado e substituído pelo novo.\033[0m"
        },
        "resposta_correta": "d"
    }
]

def carregar_dados():
    if os.path.exists(arquivo):
        with open(arquivo,'r') as f:
            return json.load(f)
    return []

def salvar_dados(lista_alunos):
    with open(arquivo, 'w') as f:
        json.dump(lista_alunos, f, indent=4)

def menu():
    print('\033[35m ====\033[0m' ' \033[1;36m MENU DE OPÇÕES \033[0m' '\033[35m ====\033[0m')
    print('')

    if usuario_logado:
        print('\033[35m1.\033[0m''\033[36m Cursos \033[0m')
        print('\033[35m2.\033[0m''\033[36m Informações de Segurança \033[0m')
        print('\033[35m3.\033[0m''\033[36m Fazer Logoff \033[0m') 
        print('\033[35m4.\033[0m''\033[36m Minhas Informações \033[0m')
        print('\033[35m0.\033[0m''\033[36m Sair \033[0m')
        escolha = input('\033[36mESCOLHA UMA OPÇÃO DE\033[0m \033[1;35m0-4: \033[m')
    else:
        print('\033[35m1.\033[0m''\033[;36m Fazer Cadastro \033[0m')
        print('\033[35m2.\033[0m ''\033[36mFazer Login \033[0m')
        print('\033[35m3.\033[0m ''\033[36mCursos \033[0m')
        print('\033[35m4.\033[0m ''\033[36mInformações de Segurança \033[0m')
        print('\033[35m0.\033[0m ''\033[36mSair \033[0m')
        escolha = input('\033[36mESCOLHA UMA OPÇÃO DE\033[0m \033[1;35m0-4: \033[m')

    return escolha

def cadastro():
    print('\033[36mVocê escolheu a opção de cadastro\033[0m')
    while True:
        nome = input('\033[36mDigite seu nome completo: \033[0m').strip()
        if len(nome) >= 10:
            nome = nome
            break
        print('\033[1;31mNome muito curto! Digite o nome completo (mínimo 10 caracteres).\033[0m')
    while True:
        nome_user = input('\033[36mDigite seu nome de usuário: \033[0m').strip()
        if nome_user:
            break
        print('\033[1;31mNome de usuário não pode estar vazio!\033[0m')
    while True:
        idade = input('\033[36mDigite sua idade: \033[0m').strip()
        if idade.isdigit():
            break
        print('\033[1;31mIdade inválida! Digite um número inteiro.\033[0m')
    while True:
        email = input('\033[36mDigite seu email: \033[0m').strip()
        if '@' in email and '.' in email:
            break
        print('\033[1;31mEmail inválido! Deve conter "@" e ".".\033[0m')
    while True:
        senha = input('\033[36mDigite sua senha (mínimo 8 caracteres e 1 caractere especial): \033[0m')
        if len(senha) < 8:
            print('\033[1;31mSenha muito curta!\033[0m')
            continue
        if not re.search(r'[^a-zA-Z0-9]', senha):
            print('\033[1;31mA senha deve conter pelo menos um caractere especial (ex: !, @, #, etc)\033[0m')
            continue
        break
    data_registro = datetime.date.today().isoformat() 

    novo_aluno = {
        'nome': nome,
        'nome_user': nome_user,
        'idade': int(idade),  
        'email': email,
        'senha': senha,
        'registro': data_registro
    }

    dados = carregar_dados()  
    dados.append(novo_aluno)
    salvar_dados(dados)      

    print(f'\033[36mUsuário {nome}, cadastrado com sucesso!\033[0m')



def excluir_usuario():
    global usuario_logado
    if not usuario_logado:
        print("\033[31mVocê precisa estar logado para excluir sua conta.\033[0m")
        return

    confirmacao = input(f"\033[33mTem certeza que deseja excluir sua conta, {usuario_logado['nome']}? (s/n): \033[0m").lower()
    if confirmacao == 's':
        dados = carregar_dados()
        dados = [u for u in dados if u['email'] != usuario_logado['email']]
        salvar_dados(dados)
        print("\033[31mSua conta foi excluída com sucesso.\033[0m")
        usuario_logado = None
    else:
        print("\033[32mA exclusão da conta foi cancelada.\033[0m")

def registrar_frequencia(modulo):
    if usuario_logado:
        if "frequencia" not in usuario_logado:
            usuario_logado["frequencia"] = {"Pensamento": 0, "Segurança": 0, "Python": 0}
        usuario_logado["frequencia"][modulo] += 1

        # Salvar no arquivo
        dados = carregar_dados()
        for u in dados:
            if u["email"] == usuario_logado["email"]:
                u["frequencia"] = usuario_logado["frequencia"]
        salvar_dados(dados)

def ver_notas():
    if not usuario_logado:
        print("\033[31mVocê precisa estar logado para ver as notas.\033[0m")
        return

    while True:
        print("\033[34m==== HISTÓRICO DE NOTAS ====\033[0m")
        notas = usuario_logado.get("notas", [])
        if not notas:
            print("\033[33mNenhuma nota registrada ainda.\033[0m")
        else:
            for nota in notas:
                print(f"\033[36mMódulo:\033[0m {nota['modulo']} - \033[36mNota:\033[0m {nota['nota']}/{nota['total']}")

        print("\033[35m1.\033[0m \033[36mVer média final de cada módulo\033[0m")
        print("\033[35m0.\033[0m \033[36mVoltar\033[0m")
        escolha = input("\033[36mEscolha uma opção: \033[0m")
        
        if escolha == '0':
            break
        elif escolha == '1':
            medias = {"Pensamento": [], "Segurança": [], "Python": []}
            for nota in notas:
                if "Pensamento" in nota["modulo"]:
                    medias["Pensamento"].append(nota["nota"] / nota["total"])
                elif "Segurança" in nota["modulo"]:
                    medias["Segurança"].append(nota["nota"] / nota["total"])
                elif "Python" in nota["modulo"]:
                    medias["Python"].append(nota["nota"] / nota["total"])
            
            print("\033[34m==== MÉDIAS FINAIS POR MÓDULO ====\033[0m")
            for modulo, lista in medias.items():
                if lista:
                    media = sum(lista) / len(lista)
                    print(f"\033[36m{modulo}:\033[0m média de {media*10:.1f}/10")
                else:
                    print(f"\033[33m{modulo}: Sem notas registradas.\033[0m")
                sleep(3.0)
        else:
            print("\033[33mOpção inválida.\033[0m")

def minhas_informacoes():
    import datetime
    if not usuario_logado:
        print("\033[31mVocê precisa estar logado para acessar essa opção.\033[0m")
        return

    print("\n\033[34m==== MINHAS INFORMAÇÕES ====\033[0m")
    print(f"\033[36mNome:\033[0m {usuario_logado['nome']}")
    print(f"\033[36mEmail:\033[0m {usuario_logado['email']}")
    print(f"\033[36mIdade:\033[0m {usuario_logado['idade']}")

    # Curso mais acessado
    frequencia = usuario_logado.get("frequencia", {"Pensamento": 0, "Segurança": 0, "Python": 0})
    curso_mais = max(frequencia, key=frequencia.get)
    print(f"\033[36mCurso mais acessado:\033[0m {curso_mais} ({frequencia[curso_mais]} vez(es))")
    print("\033[36mAcessos por curso:\033[0m")
    for curso, acessos in frequencia.items():
        print(f" - {curso}: {acessos} vez(es)")

    # Tempo na plataforma
    if 'registro' not in usuario_logado:
        usuario_logado['registro'] = str(datetime.date.today())
        dados = carregar_dados()
        for u in dados:
            if u['email'] == usuario_logado['email']:
                u['registro'] = usuario_logado['registro']
        salvar_dados(dados)

    data_registro = datetime.datetime.strptime(usuario_logado['registro'], "%Y-%m-%d").date()
    dias_na_plataforma = (datetime.date.today() - data_registro).days
    print(f"\033[36mTempo na plataforma:\033[0m {dias_na_plataforma} dia(s)")
     #Conlusão de Cursos

    conclusao = usuario_logado.get("conclusao", {})
    print(f"\033[36mStatus dos cursos:\033[0m")
    for curso in ["Pensamento", "Segurança", "Python"]:
        status = conclusao.get(curso, "em andamento")
        print(f" - {curso}: {status}")
    
    print("\n\033[35m1.\033[0m \033[36mExcluir minha conta\033[0m")
    print('\033[35m6.\033[0m \033[36mRecuperação de cursos\033[0m')
    print("\033[35m0.\033[0m \033[36mVoltar\033[0m")
    escolha = input("\033[36mEscolha uma opção: \033[0m")
    while True:
        if escolha == '1':
            excluir_usuario()
            break
        elif escolha  == '6':
            recuperacao()
            break
        elif escolha == '0':
            break
        else:
            print('\033[31mOpção inválida!\033[0m')



def logout():
    global usuario_logado
    if usuario_logado:
        print(f'\033[36mUsuário {usuario_logado["nome"]} fez logoff.\033[0m')
        usuario_logado = None
    else:
        print('\033[33mNenhum usuário está logado.\033[0m')
usuario_logado = None

def login():
    global usuario_logado
    print('\033[36mVocê escolheu a opção de login\033[0m')
    email = input('\033[36mDigite seu email: \033[0m')
    senha = input('\033[36mDigite sua senha: \033[0m')
    usuarios = carregar_dados()
    ### laço para verificar se usuario já foi cadastrado e se a senha está correta ###
    for usuario in usuarios:
        if usuario['email'] == email and usuario['senha'] == senha:
            print('Login efetuado com sucesso !! seja bem vindo(a), {}!'.format(usuario['nome_user']))
            usuario_logado = usuario # login com sucesso
            if "frequencia" not in usuario_logado:
                usuario_logado["frequencia"] = {"Pensamento": 0, "Segurança": 0, "Python": 0}

            return True
    print('email ou senha incorretos, tente novamente !')
    return False

def recuperacao():
    if not usuario_logado:
        print("\033[31mVocê precisa estar logado para fazer a recuperação.\033[0m")
        return

    if "conclusao" not in usuario_logado:
        print("\033[33mVocê não finalizou nenhum curso.\033[0m")
        return

    reprovados = [curso for curso, status in usuario_logado["conclusao"].items() if status == "reprovado"]

    if not reprovados:
        print("\033[32mParabéns! Você não tem cursos reprovados.\033[0m")
        return

    print("\033[34m==== RECUPERAÇÃO ====\033[0m")
    for i, curso in enumerate(reprovados, 1):
        print(f"\033[35m{i}.\033[0m \033[36m{curso}\033[0m")
    print("\033[35m0.\033[0m \033[36mCancelar\033[0m")

    escolha = input("\033[36mDigite o número do curso que deseja refazer: \033[0m")
    if not escolha.isdigit() or int(escolha) < 0 or int(escolha) > len(reprovados):
        print("\033[31mOpção inválida.\033[0m")
        return
    if escolha == "0":
        return

    curso = reprovados[int(escolha) - 1]

    # Executar apenas os questionários, sem entrar no menu dos cursos
    if curso == "Pensamento":
        aplicar_questionario(quest_pens_12, "Pensamento 1")
        aplicar_questionario(quest_pens_34, "Pensamento 2")
    elif curso == "Segurança":
        aplicar_questionario(quest_seg12, "Segurança 1")
        aplicar_questionario(quest_seg_34, "Segurança 2")
    elif curso == "Python":
        aplicar_questionario(quest_python_1234, "Python 1")
        aplicar_questionario(quest_python_5678, "Python 2")

    print("\033[32mRecuperação finalizada. Verifique suas informações para ver se foi aprovado.\033[0m")


def aplicar_questionario(perguntas, nome_modulo="Questionário"):
    respostas_erradas = []
    pontuacao = 0

    for i, pergunta in enumerate(perguntas, start=1):
        print(f"\n\033[35mQuestão {i}:\033[0m \033[36m{pergunta['pergunta']}\033[0m")

        for letra, opcao in pergunta["opcoes"].items():
            print(f"{letra} {opcao}")

        resposta = input("\n\033[36mDigite a resposta entre a, b, c ou d: \033[0m").lower()

        if resposta == pergunta["resposta_correta"]:
            print("\033[32mCorreto!\033[0m")
            pontuacao += 1
        else:
            print("\033[31mIncorreto!\033[0m")
            respostas_erradas.append({
                "numero": i,
                "pergunta": pergunta["pergunta"],
                "resposta_correta": pergunta["resposta_correta"],
                "sua_resposta": resposta
            })

        sleep(1.2)

    # Resultado final
    print("\n\033[34m==== RESULTADO FINAL ====\033[0m")
    print(f"\033[1;36mSua nota: {pontuacao}/{len(perguntas)}\033[0m")

    if respostas_erradas:
        print("\n\033[33mVocê errou as seguintes questões:\033[0m")
        for erro in respostas_erradas:
            print(f"\033[31mQuestão {erro['numero']}:\033[0m {erro['pergunta']}")
            print(f" - \033[36mSua resposta:\033[0m {erro['sua_resposta']}")
            print(f" - \033[32mResposta correta:\033[0m {erro['resposta_correta']}\n")
    else:
        print("\033[32mParabéns! Você acertou tudo!\033[0m")

    # Salvar nota no perfil do usuário
    if usuario_logado:
        if "notas" not in usuario_logado:
            usuario_logado["notas"] = []
        usuario_logado["notas"].append({
            "modulo": nome_modulo,
            "nota": pontuacao,
            "total": len(perguntas)
        })
        dados = carregar_dados()
        for u in dados:
            if u['email'] == usuario_logado['email']:
                u['notas'] = usuario_logado['notas']
        salvar_dados(dados)
        # Verificar conclusão do curso
    if usuario_logado:
        modulos = [n for n in usuario_logado["notas"] if nome_modulo.split()[0] in n["modulo"]]
        if len(modulos) >= 2:
            media = sum(n["nota"] / n["total"] * 10 for n in modulos) / len(modulos)
            curso = nome_modulo.split()[0]
            if media >= 6:
                status = "aprovado"
            else:
                status = "reprovado"

            if "conclusao" not in usuario_logado:
                usuario_logado["conclusao"] = {}
            usuario_logado["conclusao"][curso] = status

            dados = carregar_dados()
            for u in dados:
                if u["email"] == usuario_logado["email"]:
                    u["conclusao"] = usuario_logado["conclusao"]
            salvar_dados(dados)


def seguranca():
    sleep(1.5)
    print('')
    while True:
        print('\033[35m ==========\033[0m' ' \033[1;36m SEGURANÇA \033[0m' '\033[35m ==========\033[0m')
        print('')
        print('\033[35m1\033[0m. \033[36mPOLITICA DE PRIVACIDADE\033[0m')
        print('\033[35m2.\033[0m \033[36mTermos da LGPD\033[0m')
        print('\033[35m0.\033[0m \033[36mVoltar\033[0m')

        escolha_3 = input('\033[36mEscolha uma opção entre\033[0m \033[35m0-2: \033[0m')
        if escolha_3 == '0':
            break
        elif escolha_3 == '1':
            politica_privacidade()
        elif escolha_3 == '2':
            lgpd_termos()
        else:
            print('\033[31mOpção inválida!\033[0m')

def lgpd_termos():
    while True:
        sleep(1.5)
        print('\033[35m ==================\033[0m' ' \033[1;36m LGPD \033[0m' '\033[35m ==================\033[0m')
        print('''\033[36m
A Lei Geral de Proteção de Dados (LGPD) (Lei nº 13.709/2018) 
regulamenta o tratamento de dados pessoais no Brasil
\033[0m''')
        print('')
        sleep(1.5)
        print('\033[35m1.\033[0m \033[36mO QUE É LGPD? \033[0m')
        print('''\033[36m
A LGPD (Lei Geral de Proteção de Dados) estabelece regras sobre a coleta,
armazenamento, tratamento e compartilhamento de dados pessoais, 
garantindo mais segurança e transparência aos usuários.\033[0m''')
        print('')
        sleep(1.5)
        print('\033[35m2.\033[0m \033[36mPRINCIPIOS DA LGPD \033[0m')
        print('''\033[36m
A lei se baseia em princípios fundamentais, como:
Finalidade: Os dados são coletados para um propósito específico e legítimo.
Necessidade: Apenas os dados estritamente necessários são coletados.
Transparência: O usuário será informado sobre o uso dos dados.
Segurança: Medidas serão adotadas para proteger os dados contra acessos não autorizados.
Consentimento: O usuário deve autorizar o uso de seus dados de forma clara e livre.\033[0m''')
        print('')
        sleep(1.5)
        print('\033[35m3.\033[0m \033[36mDIREITOS DO USUARIO\033[0m')
        print('''\033[36m
Saber quais dados estão sendo coletados.
Solicitar a correção de informações incorretas.
Pedir a exclusão dos seus dados.
Revogar o consentimento para o uso dos dados.\033[0m''')
        print('')
        sleep(1.5)
        print('\033[35m4.\033[0m \033[36mCOMO PROTEGEMOS SEUS DADOS\033[0m')
        print('''\033[36m
Utilizamos medidas de segurança para proteger seus dados contra acessos indevidos.
Seus dados são usados apenas para os fins necessários e permitidos por você.
Não compartilhamos seus dados com terceiros sem sua autorização.\033[0m''')
        print('')
        escolha_5 = input('\033[36mDigite 0 para voltar: \033[0m')
        if escolha_5 == '0':
            break
        else:
            print('\033[36mopção inválida, digite 0 para voltar:\033[0m')

def politica_privacidade():
    while True:
        sleep(1.5)
        print(
            '\033[35m ==================\033[0m' ' \033[1;36m POLITICA DE PRIVACIDADE \033[0m' '\033[35m ==================\033[0m')
        print('''
        \033[36m
Esta politica de privacidade explica como a ClickEdu 
coleta, usa, armazena, e protege os dados pessoais de 
seus usuários, em conformidade com a lei geral de 
proteção de dados pessoais (lei nº13.709/2018-LGPD 
o marco civil da internet (lei nº13.965/2014) 
e outras normas aplicáveis.\033[0m
        ''')
        sleep(1.5)
        print('\033[35m2.\033[0m \033[36mDADOS COLETADOS\033[0m')
        print('''\033[36m
2.1. Dados fornecidos pelo usuário:
Nome completo;
Endereço de e-mail;

2.2. Dados coletados automaticamente:
Endereço IP;
Informações sobre o dispositivo;
Histórico de acesso e interação com a plataforma.\033[0m''')
        sleep(1.5)
        print('')
        print('\033[35m3.\033[0m \033[36mFINALIDADE DO TRATAMENTO DOS DADOS\033[0m')
        print('''\033[36m
Os dados coletados são utilizados para:
Criar e gerenciar contas dos usuários;
Disponibilizar cursos e conteúdo educacional;
Melhorar a experiência do usuário na plataforma;
Cumprir obrigações legais e regulatórias;
Realizar comunicação com o usuário sobre atualizações e serviços.\033[0m''')
        sleep(1.5)
        print('')
        print('\033[35m4.\033[0m \033[36mCOMPARTILHAMENTO DE DADOS\033[0m')
        print('''\033[36m
Não compartilhamos informações de identificação pessoal publicamente 
ou com terceiros, exceto quando exigido por lei.\033[0m''')
        sleep(1.5)
        print('')
        print('\033[35m5.\033[0m \033[36mSEGURANÇA DOS DADOS\033[0m')
        print('''\033[36m
A ClickEdu adota medidas técnicas e administrativas para proteger
os dados pessoais contra acessos não autorizados, vazamentos e 
outros incidentes.\033[0m''')
        sleep(1.5)
        print('')
        print('\033[35m6.\033[0m \033[36mDIREITO DO TITULAR DOS DADOS\033[0m')
        print('''\033[36m
O usuário pode exercer seus direitos previstos na LGPD, incluindo:
Confirmação da existência de tratamento de dados;
Acesso aos dados pessoais;
correção de dados incompletos, inexatos ou desatulizados;
Solicitação de exclusão de dados desnecessários;
revogação do consentimento para uso de dados.

O uso continuado de nossso site será considerado como aceitação
de nossas práticas acerca da privacidade e informações pessoais.
Se você tiver alguma duvida sobre como lidamos com dados do 
usuário e informações pessoais, entre em contato pelo
e-mail: suport@clickedu.com.br\033[0m''')
        sleep(1.5)
        print('')
        print('\033[35m7.\033[0m \033[36mRETENÇÃO E EXCLUSÃO DOS DADOS\033[0m')
        print('''\033[36m
Os dados serão armazenados pelo tempo necessário para cumprir as 
finalidades mencionadas, respeitando prazos legais e regulatórios.
Após esse período, os dados serão anonimizados ou excluídos de forma segura.\033[0m''')
        sleep(1.5)
        print('')
        print('\033[35m8.\033[0m \033[36mALTERAÇÕES NA POLITICA DE PRIVACIDADE\033[0m')
        print('''\033[36m
A ClickEdu pode atualizar esta Política de Privacidade periodicamente. 
Os usuários serão notificados sobre alterações relevantes.\033[0m''')
        sleep(1.5)
        print('')
        print('\033[35m9.\033[0m \033[36mRESPONSABILIDADE DO USUÁRIO\033[0m')
        print('''\033[36m
O usuário se compromete a fazer uso adequado dos conteúdos e da informação 
que a ClickEdu oferece no site e, com caráter enunciativo, mas não limitativo:
A) Não se envolver em atividades que sejam ilegais ou contrárias à boa-fé e 
à ordem pública; B) Não difundir propaganda ou conteúdo de natureza racista, 
xenofóbica, jogos de azar, qualquer tipo de pornografia, de apologia ao 
terrorismo ou contra os direitos humanos; C) Não causar danos aos sistemas 
físicos (hardwares) e lógicos (softwares) da ClickEdu, de seus fornecedores
ou terceiros, nem introduzir ou disseminar vírus informáticos ou quaisquer 
outros sistemas de hardware ou software que possam causar danos anteriormente 
mencionados.\033[0m''')
        sleep(1.5)
        print('')
        print('\033[35m10.\033[0m \033[36mCONTATO\033[0m')
        print('''\033[36m
Em caso de dúvidas sobre esta Política de Privacidade, 
entre em contato pelo e-mail: suport@clickedu.com.br.\033[0m''')
        print('')
        escolha_4 = input('\033[36mDigite 0 para voltar: \033[0m')
        if escolha_4 == '0':
            break
        else:
            print('\033[36mopção inválida, digite 0 para voltar:\033[0m')

def cursos_menu():
    if not usuario_logado:
        print('\033[31mVocê precisa estar logado para acessar os cursos!\033[0m')
        return
    while True:
        print('\033[35m ==========\033[0m' ' \033[1;36m MENU DE CURSOS \033[0m' '\033[35m ==========\033[0m')
        print('')
        print('\033[35m1.\033[0m \033[36mPensamento Lógico computacional\033[0m')
        print('\033[35m2.\033[0m \033[36mSegurança Digital\033[0m')
        print('\033[35m3.\033[0m \033[36mprogramação em python\033[0m')
        print('\033[35m4.\033[0m \033[36mVer Notas dos Questionários\033[0m')
        print('\033[35m0.\033[0m \033[36mVoltar\033[0m')
        escolha_2 = input('\033[36mEscolha uma opção de\033[0m \033[35m0-4: \033[0m')
        if escolha_2 == '1':
            pensamento()
        elif escolha_2 == '2':
            seguranca_digital()
        elif escolha_2 == '3':
            python()
        elif escolha_2 == '4':
            ver_notas()
        elif escolha_2 == '0':
            break

def pensamento():
    registrar_frequencia("Pensamento")
    while True:
        sleep(2)
        print('\033[35m ==========\033[0m' ' \033[1;36m PENSAMENTO LOGICO COMPUTACIONAL \033[0m' '\033[35m ==========\033[0m')
        print('\033[35m1.\033[0m \033[36mMODULO 1\033[0m')
        print('\033[35m2.\033[0m \033[36mMODULO 2\033[0m')
        print('\033[35m3.\033[0m \033[36mMODULO 3\033[0m')
        print('\033[35m4.\033[0m \033[36mMODULO 4\033[0m')
        print('\033[35m5.\033[0m \033[36mQUESTIONARIOS\033[0m')
        print('\033[35m0.\033[0m \033[36mVoltar\033[0m')
        escolha_pensamento = input('\033[36mEscolha uma opção de\033[0m \033[35m0-5: \033[0m')
        if escolha_pensamento == '1':
            modpens01()
        elif escolha_pensamento == '2':
            modpens02()
        elif escolha_pensamento == '3':
            modpens03()
        elif escolha_pensamento == '4':
            modpens04()
        elif escolha_pensamento == '5':
            quest_pens_modulos()
        elif escolha_pensamento == '0':
            break
        else:
            pensamento()

def modpens01():
    while True:
        print('\033[35m ==========\033[0m' ' \033[1;36m MODULO 01 \033[0m' '\033[35m ==========\033[0m')
        sleep(2.0)
        print('\033[36mFUNDAMENTOS DO PENSAMENTO COMPUTACIONAL\033[0m')
        print('''\033[36m
Objetivo Geral: Apresentar o que é o pensamento computacional, desenvolver suas habilidades-chave e 
mostrar como ele pode ser usado para resolver problemas de forma lógica, organizada e eficiente — 
dentro e fora da programação.

1. O que é Pensar Computacionalmente?
Definição: Pensar computacionalmente é aplicar princípios da ciência da computação para resolver problemas
de maneira sistemática. Isso não significa necessariamente programar, mas estruturar o pensamento de forma
lógica, eficiente e estratégica.

Exemplo cotidiano:
Organizar sua rotina semanal pode ser feito de forma computacional:
Que tarefas são fixas?
Quais são prioridades?
O que pode ser feito em paralelo?

2. As Quatro Habilidades-Chave do Pensamento Computacional
a) Abstração
Focar no que é essencial e ignorar o que é desnecessário.
Exemplo: Ao pedir comida por um aplicativo, você abstrai todo o processo da cozinha, focando apenas no 
cardápio e no pedido.
b) Decomposição
Dividir um problema grande em partes menores e mais simples.
Exemplo: Planejar uma viagem envolve separar passagens, hospedagem, passeios, orçamento etc.
c) Reconhecimento de Padrões
Identificar semelhanças ou repetições para prever comportamentos ou otimizar tarefas.
Exemplo: Se toda segunda-feira você gasta mais tempo no trânsito, pode antecipar essa tendência.
d) Algoritmos
Sequência de passos claros para resolver um problema.
Exemplo: Receita de bolo — siga um passo a passo para alcançar um resultado.

3. Aplicações Fora da Programação
Essas habilidades são úteis em diversas áreas:
Educação: organizar conteúdo e métodos de ensino.
Negócios: otimizar processos, tomada de decisão baseada em dados
Saúde: protocolos de atendimento ou triagem.
Vida pessoal: organização financeira, planejamento de estudos, hábitos saudáveis.
\033[0m''')
        escolha_pen01 = input('\033[36mDigite 0 para voltar:  \033[m')
        if escolha_pen01 == '0':
            break
        else:
            escolha_pen01 = input('\033[36mEscolha inválida \033[m')

def modpens02():
    while True:
        print('\033[35m ==========\033[0m' ' \033[1;36m MODULO 02 \033[0m' '\033[35m ==========\033[0m')
        sleep(2.0)
        print('\033[36mRACIOCÍNIO LÓGICO E PROPOSIÇÕES\033[0m')
        print('''\033[36m
Objetivo Geral: Desenvolver a capacidade de pensar logicamente, entender o que são proposições e como 
elas se combinam por meio da lógica binária (Verdadeiro/Falso), preparando a base para decisões algorítmicas
 e codificação futura.

1. O que são Proposições?
Definição: Uma proposição é uma afirmação que pode ser verdadeira (V) ou falsa (F), mas nunca as duas ao 
mesmo tempo.
Exemplos de proposições:
"O céu é azul." Certo (Pode ser avaliada como verdadeira.)
"2 + 2 = 5." Errada  (Pode ser avaliada como falsa.)
Exemplos de frases que não são proposições:
"Feche a janela." (É um comando, não pode ser julgada como V ou F.)
"Será que vai chover?" (É uma pergunta, sem valor lógico.)

2. Lógica Binária: Verdadeiro (V) ou Falso (F)
A base do raciocínio computacional está na lógica binária, onde só existem dois valores possíveis:
(Verdadeiro) ou 0 (Falso).
Importância: É o mesmo princípio usado em circuitos eletrônicos e programação — tudo se resume a decisões 
lógicas com base nesses dois valores.

3. Lógica Verbal e Numérica
a) Exercícios de Lógica Verbal:
Problemas de dedução.
Ex: "Se todo gato mia, e se Bichano mia, então Bichano é gato?"
b) Exercícios de Lógica Numérica:
Sequências lógicas: 2, 4, 6, _, _
Quebra-cabeças: “Maria tem o dobro da idade de João, que tem 10. Quantos anos Maria tem?”
\033[0m''')
        escolha_pen02 = input('\033[36mDigite 0 para voltar:  \033[m')
        if escolha_pen02 == '0':
            break
        else:
            escolha_pen02 = input('\033[36mEscolha inválida \033[m')

def modpens03():
    while True:
        print('\033[35m ==========\033[0m' ' \033[1;36m MODULO 03 \033[0m' '\033[35m ==========\033[0m')
        sleep(2.0)
        print('\033[36mESTRUTURA DE PROBLEMAS E ALGORISTMOS\033[0m')
        print('''\033[36m
Objetivo Geral: Ensinar o aluno a identificar, entender e organizar problemas de forma lógica, estruturando
soluções através de algoritmos simples. Isso estabelece as bases para qualquer atividade de programação ou 
automação de tarefas.

1. O que é um Algoritmo?
Definição: Um algoritmo é uma sequência finita de passos organizados e lógicos para resolver um problema ou 
realizar uma tarefa.

Exemplos simples de algoritmos do dia a dia:
Receita de bolo
Rotina matinal (acordar, escovar os dentes, tomar café...)
Instruções para montar um móvel
Palavra-chave: Clareza. Um bom algoritmo deve ser claro, objetivo e executável.

2. Componentes Básicos de um Algoritmo
Entrada
Dados ou informações necessárias para começar.
Exemplo: Para fazer um suco, você precisa de frutas, água e açúcar.

Processamento
O que será feito com os dados.
Exemplo: Bater os ingredientes no liquidificador.

Saída
O resultado final.
Exemplo: O suco pronto.

3. Representando Problemas como Sequência Lógica
Passo a Passo para Estruturar um Problema:
Compreender o problema
O que está sendo pedido?
Quais dados são fornecidos?
Identificar as partes (entrada, processamento e saída)
Criar a sequência de etapas
Organizar cada ação necessária para alcançar o objetivo.
Testar mentalmente ou com exemplos
Isso ajuda a ver se o algoritmo resolve de fato o problema.

Exemplos Práticos
Exemplo 1: Fazer um sanduíche
Entrada: pão, queijo, presunto
Processamento: colocar o queijo e o presunto entre os pães
Saída: sanduíche pronto

Exemplo 2: Verificar se um número é par
Entrada: número
Processamento: dividir o número por 2 e verificar o resto
Saída: se o resto for zero, é par; senão, é ímpar
\033[0m''')
        escolha_pen03 = input('\033[36mDigite 0 para voltar:  \033[m')
        if escolha_pen03 == '0':
            break
        else:
            escolha_pen03 = input('\033[36mEscolha inválida \033[m')

def modpens04():
    while True:
        print('\033[35m ==========\033[0m' ' \033[1;36m MODULO 04 \033[0m' '\033[35m ==========\033[0m')
        sleep(2.0)
        print('\033[36mREPRESENTAÇÃO DE ALGORISTMOS\033[0m')
        print('''\033[36m
Objetivo Geral: Ensinar o aluno a traduzir um algoritmo mental ou escrito em diferentes formas de 
representação, como narrativa, fluxograma e pseudocódigo, preparando para transições futuras à programação 
real.

1. Por que Representar um Algoritmo?
Representar um algoritmo de forma estruturada permite:
Melhor visualização do processo
Facilidade na identificação de erros
Clareza ao comunicar soluções com outras pessoas
Base para codificação em linguagens de programação

2. Tipos de Representações: 
a) Narrativa (Descrição Informal)
Definição: Representação do algoritmo como uma sequência de instruções em linguagem natural, de forma 
simples e direta.
Exemplo:
Algoritmo para preparar um café:
1. Ferva a água
2. Coloque o pó de café no filtro
3. Despeje a água sobre o pó
4. Deixe o café coar
5. Sirva na xícara

Vantagem: Fácil de escrever e entender
Limitação: Pode ser ambíguo ou impreciso

b) Fluxograma (Representação Gráfica)
Definição: Representa o algoritmo com símbolos gráficos padronizados, facilitando a visualização do 
fluxo de decisões e processos.

Principais símbolos:
Símbolo	           Nome	               Função
Elipse	        Início/Fim	      Indica onde começa/termina
Retângulo	     Processo	      Ações ou cálculos
Losango	         Decisão	      Condições (sim/não)
Seta	         Setas	          Indicam o fluxo do algoritmo

 Vantagem: Visual, ótimo para iniciantes
Limitação: Exige familiaridade com os símbolos

c) Pseudocódigo (Linguagem Estruturada)
Definição: Forma textual parecida com um código de programação, mas escrita em linguagem natural 
estruturada, com comandos claros e organizados.

Exemplo:
Início
  Ler número
  Se número % 2 = 0 então
    Escrever "Número é par"
  Senão
    Escrever "Número é ímpar"
Fim

Vantagem: Aproxima o aluno da lógica de programação
Limitação: Requer organização e padronização

Comparando as Representações:
Representação	       Linguagem	     Complexidade	     Quando usar?
Narrativa	           Natural	          Baixa	             Início do aprendizado
Fluxograma	           Visual	          Média	             Visualização de lógica e decisões
Pseudocódigo	       Estruturada	      Média/Alta	     Transição para programação
\033[0m''')
        escolha_pen04 = input('\033[36mDigite 0 para voltar:  \033[m')
        if escolha_pen04 == '0':
            break
        else:
            escolha_pen04 = input('\033[36mEscolha inválida \033[m')

def quest_pens_modulos():
    from time import sleep
    while True:
        print('\033[35m ==========\033[0m' ' \033[1;36m QUESTIONÁRIOS - PENSAMENTO COMPUTACIONAL \033[0m' '\033[35m ==========\033[0m')
        print('\033[35m1.\033[0m \033[36mMódulo 1 e 2\033[0m')
        print('\033[35m2.\033[0m \033[36mMódulo 3 e 4\033[0m')
        print('\033[35m3.\033[0m \033[36mVoltar\033[0m')
        escolha_quest_pens = input('\033[36mEscolha uma opção entre\033[0m \033[35m1-3: \033[0m')

        if escolha_quest_pens == '1':
            print('\033[35m ==========\033[0m' ' \033[1;36mPENSAMENTO COMPUTACIONAL\033[0m' '\033[35m ==========\033[0m')
            aplicar_questionario(quest_pens_12, "Pensamento Computacional - Módulo 1 e 2")
        elif escolha_quest_pens == '2':
            print('\033[35m ==========\033[0m' ' \033[1;36mESTRUTURA E REPRESENTAÇÃO DE ALGORITMOS\033[0m' '\033[35m ==========\033[0m')
            aplicar_questionario(quest_pens_34, "Pensamento Computacional - Módulo 3 e 4")
        elif escolha_quest_pens == '3':
            break
        else:
            print('\033[31mOpção inválida!\033[0m')
        sleep(1.5)

def quest_seg_modulos():
    while True:
        print('\033[35m ==========\033[0m' ' \033[1;36m QUESTIONÁRIOS - SEGURANÇA DIGITAL \033[0m' '\033[35m ==========\033[0m')
        print('\033[35m1.\033[0m \033[36mMódulo 1 e 2\033[0m')
        print('\033[35m2.\033[0m \033[36mMódulo 3 e 4\033[0m')
        print('\033[35m3.\033[0m \033[36mVoltar\033[0m')
        escolha_quest_seg = input('\033[36mEscolha uma opção entre\033[0m \033[35m1-3: \033[0m')

        if escolha_quest_seg == '1':
            print('\033[35m ==========\033[0m' ' \033[1;36mSEGURANÇA DIGITAL\033[0m' '\033[35m ==========\033[0m')
            aplicar_questionario(quest_seg12, "Segurança Digital - Módulo 1 e 2")
        elif escolha_quest_seg == '2':
            print('\033[35m ==========\033[0m' ' \033[1;36mAMEAÇAS E BOAS PRÁTICAS EM SEGURANÇA DIGITAL\033[0m' '\033[35m ==========\033[0m')
            aplicar_questionario(quest_seg_34)
        elif escolha_quest_seg == '3':
            break
        else:
            print('\033[31mOpção inválida!\033[0m')
        sleep(1.5)

def quest_python_modulos():
    while True:
        print('\033[35m ==========\033[0m' ' \033[1;36m QUESTIONÁRIOS - PROGRAMAÇÃO EM PYHON \033[0m' '\033[35m ==========\033[0m')
        print('\033[35m1.\033[0m \033[36mMódulo 1, 2, 4 E 4\033[0m')
        print('\033[35m2.\033[0m \033[36mMódulo 5, 6, 7 e 8\033[0m')
        print('\033[35m3.\033[0m \033[36mVoltar\033[0m')
        escolha_quest_python = input('\033[36mEscolha uma opção entre\033[0m \033[35m1-3: \033[0m')

        if escolha_quest_python == '1':
            print('\033[35m ==========\033[0m' ' \033[1;36mSEGURANÇA DIGITAL\033[0m' '\033[35m ==========\033[0m')
            aplicar_questionario(quest_python_1234, "Python - Módulo 1 ao 4")
        elif escolha_quest_python == '2':
            print('\033[35m ==========\033[0m' ' \033[1;36mAMEAÇAS E BOAS PRÁTICAS EM SEGURANÇA DIGITAL\033[0m' '\033[35m ==========\033[0m')
            aplicar_questionario(quest_python_5678, "Python - Módulo 5 ao 8")
        elif escolha_quest_python == '3':
            break
        else:
            print('\033[31mOpção inválida!\033[0m')
        sleep(1.5)

def seguranca_digital():
    registrar_frequencia("Segurança")
    while True:
        sleep(2)
        print('\033[35m ==========\033[0m' ' \033[1;36m SEGURANÇA DIGITAL \033[0m' '\033[35m ==========\033[0m')
        print('\033[35m1.\033[0m \033[36mMODULO 1\033[0m')
        print('\033[35m2.\033[0m \033[36mMODULO 2\033[0m')
        print('\033[35m3.\033[0m \033[36mMODULO 3\033[0m')
        print('\033[35m4.\033[0m \033[36mMODULO 4\033[0m')
        print('\033[35m5.\033[0m \033[36mQUESTIONARIOS\033[0m')
        print('\033[35m0.\033[0m \033[36mVoltar\033[0m')
        escolha_seguranca = input('\033[36mEscolha uma opção de\033[0m \033[35m0-5: \033[0m')
        if escolha_seguranca == '1':
            modseg01()
        elif escolha_seguranca == '2':
            modseg02()
        elif escolha_seguranca == '3':
            modseg03()
        elif escolha_seguranca == '4':
            modseg04()
        elif escolha_seguranca == '5':
            quest_seg_modulos()
        elif escolha_seguranca == '0':
            break
        else:
            seguranca_digital()

def modseg01():
    while True:
        print('\033[35m ==========\033[0m' ' \033[1;36m MODULO 01 \033[0m' '\033[35m ==========\033[0m')
        sleep(2.0)
        print('\033[36mO QUE É SEGURANCA DIGITAL ?\033[0m')
        print('''\033[36m
Segurança digital é o conjunto de práticas, ferramentas e tecnologias usadas para proteger informações
e sistemas digitais contra acessos não autorizados, ataques, danos ou roubo. Ela tem três objetivos 
principais:
1. Confidencialidade: garantir que só pessoas autorizadas tenham acesso às informações.
2. Integridade: assegurar que os dados não sejam alterados de forma indevida ou corrompidos.
3. Disponibilidade: manter os sistemas e dados acessíveis sempre que forem necessários.

Esses princípios são conhecidos como CIA (Confidentiality, Integrity, Availability) e formam a base da 
segurança digital.
Ameaças mais comuns à segurança digital:
Hackers = pessoas que exploram vulnerabilidades nos sistemas para obter acesso não autorizado.
Nem todo hacker é mal-intencionado (alguns ajudam a encontrar falhas), mas aqui estamos falando dos que 
causam danos, roubos ou invasões.
Malware = É a abreviação de “software malicioso”. Pode incluir:
Vírus – programas que se espalham e prejudicam os dispositivos.
Spyware – espionam suas atividades para roubar dados.
Ransomware – sequestram seus dados e exigem pagamento para liberar.
Phishing = Tentativas de enganar você para obter informações confidenciais, como senhas ou dados bancários.
Vêm disfarçados de e-mails ou mensagens legítimas, mas são fraudes digitais.

Outros exemplos de riscos:
Ataques de negação de serviço (DDoS): sobrecarregam um sistema para tirá-lo do ar.
Roubo de identidade: uso indevido de informações pessoais para cometer fraudes.
Engenharia social: quando alguém manipula você para revelar informações, sem usar 
tecnologia diretamente.

Para refletir: Você já pensou quantas informações suas estão online? Fotos, conversas, documentos, 
dados bancários... A segurança digital é o que nos ajuda a proteger esse mundo invisível, mas tão valioso.
\033[0m''')
        escolha_seg01 = input('\033[36mDigite 0 para voltar:  \033[m')
        if escolha_seg01 == '0':
            break
        else:
            escolha_seg01 = input('\033[36mEscolha inválida \033[m')
def modseg02():
    while True:
        print('\033[35m ==========\033[0m' ' \033[1;36m MODULO 02 \033[0m' '\033[35m ==========\033[0m')
        sleep(2.0)
        print('\033[36mPOR QUE A SEGURANÇA DIGITAL É IMPORTANTE ?\033[0m')
        print('''\033[36m
Vivemos cada vez mais conectados. Compramos online, usamos aplicativos de banco, estudamos, trabalhamos
e até nos relacionamos através de plataformas digitais. Com tudo isso, nossos dados estão constantemente
circulando pela internet — e é aí que a segurança digital se torna essencial.
A segurança digital protege a vida digital das pessoas e das organizações, evitando prejuízos financeiros, 
emocionais e sociais.
Principais razões pelas quais ela é tão importante:

1. Proteção de dados
A segurança digital impede que seus dados sejam acessados, alterados ou roubados por pessoas não autorizadas. 
Imagine se alguém conseguisse acesso ao seu e-mail, às suas redes sociais ou à sua conta bancária.
Com uma boa segurança, essas informações ficam seguras contra invasões, vazamentos ou usos indevidos.

2. Preservação da privacidade
Privacidade significa ter controle sobre suas próprias informações. A segurança digital ajuda a garantir 
que seus dados:
Não sejam compartilhados sem sua permissão.
Não sejam usados por empresas ou criminosos para fins desconhecidos.
Não sejam expostos publicamente por falhas ou ataques.

Exemplo: Um aplicativo que coleta seus dados sem consentimento está violando sua privacidade. A segurança 
digital ajuda a evitar isso com boas práticas e regulamentações, como a LGPD (Lei Geral de Proteção de Dados).

3. Garantia de confiabilidade
Um sistema digital seguro é um sistema confiável:
Funciona corretamente.
Responde de forma estável.
Está livre de falhas causadas por vírus, ataques ou sabotagens.
Isso é essencial para serviços como:
Hospitais (onde falhas podem colocar vidas em risco),
Escolas (que guardam históricos escolares e dados de alunos),
Empresas (que dependem de sistemas para funcionar diariamente).

4. Prevenção de prejuízos financeiros e reputacionais
Ataques cibernéticos podem causar:
Roubo de dinheiro
Fraude em compras online
Clonagem de cartões
Queda na confiança do público (em empresas ou instituições)
Um simples descuido com a segurança pode gerar consequências sérias — tanto para pessoas quanto para organizações.

5. Responsabilidade social e coletiva
A segurança digital não é só um problema individual. Quando um computador é infectado, ele pode se tornar uma 
porta de entrada para atacar outros sistemas.
Manter a segurança dos seus dispositivos e dados ajuda a proteger também:
Sua família,
Seus colegas de trabalho,
E até a rede de toda uma empresa ou escola.

Para refletir:
"Privacidade e segurança não são luxos digitais – são direitos básicos."
Entender a importância da segurança digital é o primeiro passo para agir de forma mais consciente e responsável 
no mundo online.
\033[0m''')
        escolha_mod02 = input('\033[36mDigite 0 para voltar:  \033[m')
        if escolha_mod02 == '0':
            break
        else:
            escolha_mod02 = input('\033[36mEscolha inválida \033[m')
def modseg03():
    while True:
        print('\033[35m ==========\033[0m' ' \033[1;36m MODULO 03 \033[0m' '\033[35m ==========\033[0m')
        sleep(2.0)
        print('\033[36mQUAIS SÃO OS PROBLEMAS QUE AMEAÇAM NOSSA SEGURANÇA DIGITAL?\033[0m')
        print('''\033[36m
A internet oferece inúmeras facilidades, mas também é um ambiente onde diversos riscos podem comprometer
nossa segurança e privacidade. Conhecer essas ameaças é essencial para saber como se proteger.
Vamos explorar as principais formas como a segurança digital pode ser comprometida e como essas ameaças 
afetam pessoas, empresas e instituições.

1. Hackers mal-intencionados
São pessoas ou grupos que tentam acessar sistemas ou dados sem autorização, muitas vezes com objetivos 
criminosos. Eles exploram falhas de segurança ou tentam enganar os usuários para obter acesso. Podem 
roubar dados, espalhar vírus, derrubar sites ou até sequestrar sistemas inteiros (como no caso de ataques
com ransomware). Nem todo hacker é criminoso! Existem os chamados "hackers éticos" que trabalham para 
descobrir falhas e ajudar a corrigir vulnerabilidades.

2. Malware (software malicioso)
Malware é um tipo de programa criado para causar dano, roubo de informações ou controle de sistemas. 
Os principais tipos incluem:
Vírus: se anexam a arquivos e se espalham entre dispositivos.
Spyware: espiam o que o usuário faz e enviam essas informações para terceiros.
Adware: enchem a tela de anúncios e podem coletar dados sem permissão.
Ransomware: sequestram os dados e exigem pagamento para liberar o acesso.
Muitas vezes, o malware entra no sistema através de downloads suspeitos, anexos de e-mail ou sites inseguros.

3. Phishing
Phishing é uma técnica de engenharia social usada para enganar pessoas e fazer com que elas entreguem dados 
confidenciais, como senhas e números de cartão. Acontece geralmente por e-mails falsos, SMS, redes sociais 
ou até sites que imitam páginas oficiais. Essas mensagens usam urgência, ameaças ou recompensas falsas para 
persuadir o usuário.
Exemplo: um e-mail dizendo que seu banco bloqueou sua conta e pedindo para você clicar em um link e 
"verificar seus dados".

4. Ataques DDoS (Negação de Serviço Distribuída)
Nesses ataques, criminosos sobrecarregam um site ou sistema com acessos falsos, fazendo com que ele saia do ar.
São comuns contra sites de empresas, instituições públicas ou bancos. Não visam roubo de dados diretamente, mas
 sim causar prejuízos financeiros e de reputação.

5. Engenharia social
Ao invés de atacar o sistema, esses golpes exploram comportamentos humanos. São tentativas de manipular ou enganar
 as pessoas para conseguir informações ou acesso.
Podem envolver telefonemas falsos, conversas manipuladoras ou criação de laços de confiança falsos (como perfis 
falsos em redes sociais).
Exigem atenção, senso crítico e cuidado ao compartilhar informações.

6. Vazamentos de dados
Ocorrem quando informações pessoais, financeiras ou confidenciais são expostas na internet, geralmente após:
Invasões de sistemas,
Falhas de segurança, Ou falta de cuidados com o armazenamento e o compartilhamento de dados. Uma vez vazados,
esses dados podem ser usados em fraudes, extorsões ou clonagens de identidade.

Para refletir:
"A maior parte dos ataques cibernéticos não acontece por causa da tecnologia, mas por falhas humanas." 
Entender as ameaças é o primeiro passo para se proteger. No próximo módulo, você vai aprender como evitar 
esses problemas com boas práticas simples, mas eficazes.
\033[0m''')
        escolha_mod03 = input('\033[36mDigite 0 para voltar:  \033[m')
        if escolha_mod03 == '0':
            break
        else:
            escolha_mod03 = input('\033[36mEscolha inválida \033[m')
def modseg04():
    while True:
        print('\033[35m ==========\033[0m' ' \033[1;36m MODULO 04 \033[0m' '\033[35m ==========\033[0m')
        sleep(2.0)
        print('\033[36mBOAS PRATICAS PARA GARANTIR A SEGURANÇA DIGITAL\033[0m')
        print('''\033[36m
Agora que você já sabe o que é segurança digital, por que ela é importante e quais ameaças estão por aí,
 é hora de descobrir como se proteger na prática. Pequenas atitudes no dia a dia fazem uma grande diferença 
 para manter seus dados seguros.
Estas boas práticas valem tanto para uso pessoal quanto profissional, e devem fazer parte da sua rotina digital.

1. Use senhas fortes e únicas
Senhas são a primeira linha de defesa contra invasores. Uma boa senha deve:
Ter mais de 8 caracteres.
Incluir letras maiúsculas e minúsculas, números e símbolos.
Ser diferente para cada conta ou serviço.
Evite senhas óbvias como "123456", "senha" ou datas de aniversário.
Dica: Use um gerenciador de senhas para armazenar com segurança e lembrar todas as suas senhas diferentes.

2. Ative a autenticação multifator (MFA ou 2FA)
Essa medida adiciona uma camada extra de segurança além da senha.
Funciona assim: mesmo que alguém descubra sua senha, ainda será preciso uma segunda verificação, como:
Um código enviado por SMS ou e-mail,
Um aplicativo autenticador (como o Google Authenticator),
Biometria (impressão digital, reconhecimento facial).

3. Mantenha seus sistemas e programas atualizados
Atualizações não servem só para adicionar novos recursos — elas corrigem falhas de segurança que podem ser 
exploradas por hackers.
Atualize sempre seu sistema operacional, navegador, antivírus e aplicativos.
Ative as atualizações automáticas sempre que possível.

4. Cuidado com e-mails e mensagens suspeitas
Muitos ataques começam com phishing: mensagens falsas que tentam enganar você.
Fique atento a:
Links encurtados ou estranhos,
Erros de português,
Pressa ou ameaças para você agir rápido,
Solicitações de informações pessoais ou bancárias.
Nunca clique em links ou baixe arquivos de remetentes que você não conhece ou não confia.

5. Evite usar redes Wi-Fi públicas para tarefas sensíveis
Redes públicas (de cafés, aeroportos, shoppings) são práticas, mas podem ser inseguras. Evite acessar 
contas bancárias, e-mails ou redes sociais importantes em Wi-Fi público. Use VPNs (redes privadas virtuais) 
para proteger sua conexão quando for inevitável usar esse tipo de rede. 

6. Desconfie antes de compartilhar dados
Antes de preencher formulários online, dar seu CPF ou clicar em "aceito", pergunte-se:
"Esse site é confiável?"
"Essa informação é realmente necessária aqui?"
"Estou ciente do que estão fazendo com meus dados?"
Sempre prefira sites com “https://” e cadeado de segurança na barra de endereço.

7. Use antivírus e firewall
Essas ferramentas ajudam a detectar e bloquear ameaças automaticamente.
Um antivírus confiável pode impedir que malwares se instalem no seu dispositivo.
O firewall ajuda a controlar o tráfego de dados e proteger sua rede.

8. Faça backups regulares dos seus dados
Guardar cópias dos seus arquivos importantes é essencial para evitar perdas causadas por falhas, 
vírus ou ataques.
Use HDs externos, pen drives ou serviços de armazenamento em nuvem.
Faça backups com regularidade e mantenha pelo menos uma cópia offline.

9. Eduque-se e fique sempre atento
A melhor ferramenta de segurança é o conhecimento. Esteja sempre atualizado sobre novas ameaças, 
golpes e práticas de proteção.
Siga fontes confiáveis de tecnologia.
Compartilhe esse conhecimento com amigos, familiares e colegas de trabalho.

Para refletir:
"A segurança digital não é feita só de tecnologia. Ela começa com o seu comportamento."
Cada escolha que você faz online pode aproximar ou afastar um risco. Criar uma rotina de cuidados é o melhor 
caminho para navegar na internet com mais liberdade e menos preocupação.
\033[0m''')
        escolha_mod04 = input('\033[36mDigite 0 para voltar:  \033[m')
        if escolha_mod04 == '0':
            break
        else:
            escolha_mod04 = input('\033[36mEscolha inválida \033[m')

def python():
    registrar_frequencia("Python")
    while True:
        sleep(2)
        print('\033[35m ==========\033[0m' ' \033[1;36m PROGRAMAÇÃO EM PYTHON \033[0m' '\033[35m ==========\033[0m')
        print('\033[35m1.\033[0m \033[36mMODULO 1\033[0m')
        print('\033[35m2.\033[0m \033[36mMODULO 2\033[0m')
        print('\033[35m3.\033[0m \033[36mMODULO 3\033[0m')
        print('\033[35m4.\033[0m \033[36mMODULO 4\033[0m')
        print('\033[35m5.\033[0m \033[36mMODULO 5\033[0m')
        print('\033[35m6.\033[0m \033[36mMODULO 6\033[0m')
        print('\033[35m7.\033[0m \033[36mMODULO 7\033[0m')
        print('\033[35m8.\033[0m \033[36mMODULO 8\033[0m')
        print('\033[35m9.\033[0m \033[36mQUESTIONARIOS\033[0m')
        print('\033[35m0.\033[0m \033[36mVoltar\033[0m')

        escolha_python = input('\033[36mEscolha uma opção de\033[0m \033[35m1-9: \033[0m')
        if escolha_python == '1':
            modpython01()
        elif escolha_python == '2':
            modpython02()
        elif escolha_python == '3':
            modpython03()
        elif escolha_python == '4':
            modpython04()
        elif escolha_python == '5':
            modpython05()
        elif escolha_python == '6':
            modpython06()
        elif escolha_python == '7':
            modpython07()
        elif escolha_python == '8':
            modpython08()
        elif escolha_python == '9':
            quest_python_modulos()
        elif escolha_python == '0':
            break
        else:
            python()

def modpython01():
    while True:
        print('\033[35m ==========\033[0m' ' \033[1;36m MODULO 01 \033[0m' '\033[35m ==========\033[0m')
        sleep(2.0)
        print('\033[36mINTRODUÇÃO AO PYTHON\033[0m')
        print('\033[36mBreve resumo da história e uso da Linguagem Python\033[0m')
        print('''\033[36m
Python foi criado por Guido van Rossum em 1989, na Holanda, como um sucessor da linguagem ABC,
com o objetivo de ser fácil de ler, escrever e manter. A primeira versão oficial, Python 0.9.0,
foi lançada em 1991, já com funcionalidades como tratamento de exceções, tipos de dados básicos
(strings, listas, dicionários), e módulos. Desde então, o Python evoluiu com a ajuda de uma
comunidade ativa de desenvolvedores. Ele se tornou uma linguagem de código aberto, mantida pela
Python Software Foundation (PSF). Atualmente, o Python está em sua versão 3.x, com atualizações
frequentes que melhoram o desempenho, a segurança e a clareza da linguagem.
Python é conhecido por sua simplicidade e versatilidade. Por isso, é utilizado em diversas áreas:

- Desenvolvimento Web com frameworks como Django e Flask, é possível criar sites e aplicações 
web completos;
- Ciência de Dados e Análise Estatística: bibliotecas como Pandas, NumPy, Matplotlib e Scikit-learn
 fazem do Python uma das linguagens mais usadas por cientistas de dados;
 - Inteligência Artificial e Machine Learning: com bibliotecas como TensorFlow, PyTorch e Keras, 
 Python é a principal linguagem para criar modelos inteligentes;
- Automação de Tarefas: muitas pessoas usam Python para automatizar tarefas repetitivas no computador, 
como organização de arquivos, envio de e-mails ou raspagem de dados da internet;
- Desenvolvimento de Jogos: com bibliotecas como Pygame, é possível criar jogos 2D simples para fins 
educativos ou de entretenimento;
- Educação: por ser fácil de aprender, Python é amplamente usado em cursos introdutórios de programação 
ao redor do mundo.

Por que aprender Python?
Sintaxe clara e fácil de entender;
Comunidade grande e ativa;
Documentação rica;
Usado por empresas como Google, NASA, Netflix e Spotify; Ótimo para iniciantes e poderoso para profissionais.
 \033[0m''')
        sleep(2.0)
        print('')
        print('\033[36mCOMO INSTALAR O PYTHON (PASSO A PASSO)\033[0m')
        print('''\033[36m
Passo 1: Acesse o site oficial
Vá até o site: https://www.python.org

Passo 2: Vá até a seção de downloads
Clique na aba “Downloads”
O site detecta automaticamente seu sistema (Windows, macOS ou Linux)
Clique em “Download Python [download the latest version/download da versão mais recente]”

Passo 3: Execute o instalador
Após o download, abra o arquivo baixado
Antes de clicar em “Install Now”, marque a opção:
“Add Python to PATH” (muito importante!)

Passo 4: Instalação
Clique em “Install Now”
Aguarde o processo terminar
Ao final, clique em “Close”

Passo 5: Verificar se foi instalado
Abra o Prompt de Comando (Windows) ou Terminal (macOS/Linux)
Digite: python 
Se aparecer algo como Python 3.x.x, está instalado corretamente!
Caso não apareça, reinstale o programa.

\033[0m''')
        sleep(2.0)
        print('')
        print('\033[36mCOMO USAR O TERMINAL E EDITORES COM PYTHON\033[0m')
        print('''\033[36m
1 . Usando o Terminal
O terminal (ou prompt de comando) é a forma mais direta de rodar Python.
Passo a passo:
Abra o terminal:
Windows: Pesquise por cmd ou Prompt de Comando
macOS/Linux: Use o app "Terminal"
Digite: Python
Isso abre o modo interativo (REPL), onde você pode digitar comandos Python direto na tela.
Para rodar um arquivo .py salvo, vá até a pasta do arquivo e digite:
python nome_do_arquivo.py

2. Usando o VSCode (Visual Studio Code)
O VSCode é um editor leve e muito usado para Python.
Passo a passo:
Baixe e instale: https://code.visualstudio.com
Abra o VSCode e instale a extensão “Python” (ícone de quadrado no menu lateral > buscar "Python" > instalar).
Abra uma pasta onde ficará seu projeto.
Crie um novo arquivo com final .py, por exemplo: teste.py
Escreva o código Python, como:
print("Hello, World!")
Clique no botão de “Play” no topo direito ou pressione Ctrl + F5 para executar o programa.

3. Usando o PyCharm
O PyCharm é um IDE completo, ideal para projetos maiores.
Passo a passo:
Baixe e instale: https://www.jetbrains.com/pycharm/
Use a versão Community (gratuita)
Crie um novo projeto
Escolha a versão do Python instalada (geralmente o PyCharm detecta automaticamente)
Crie um novo arquivo .py
Escreva o código e clique com o botão direito > “Run 'nome_do_arquivo'”

\033[0m''')
        escolha_pymod01 = input('\033[36mDigite 0 para voltar:  \033[m')
        if escolha_pymod01 == '0':
            break
        else:
            escolha_pymod01 = input('\033[36mEscolha inválida \033[m')
def modpython02():
    while True:
        print('\033[35m ==========\033[0m' ' \033[1;36m MODULO 02 \033[0m' '\033[35m ==========\033[0m')
        sleep(2.0)
        print('\033[36mVARIAVEIS E TIPOS DE DADOS\033[0m')
        print('''\033[36m
Neste módulo, vamos aprender a declarar variáveis e a trabalhar com os tipos de dados mais comuns em 
Python: números, strings e booleanos, além de converter tipos (casting).

1. O que são variáveis?
Variáveis são espaços na memória onde podemos guardar valores para usar depois.
Exemplo:
| nome = "Ana" |
| idade = 25 |
Aqui, nome guarda uma string e idade guarda um número inteiro.

2. Tipos de dados

a) Números
int → Números inteiros (sem vírgula)
float → Números decimais (com vírgula, mas em Python usa-se o ponto .)
Exemplo:
| idade = 30          # int |
| altura = 1.75       # float |

b) Strings
Usadas para armazenar textos
Sempre entre aspas simples ou aspas duplas
Exemplo:
| nome = "Carlos" |
| frase = 'Python é fácil!' |

c) Booleanos
Representam valores verdadeiros ou falsos
Em Python, usamos True e False (com letra maiúscula)
 Exemplo:
| maior_de_idade = True |
| tem_carteira = False |

3. Conversão de Tipos (Casting)
Às vezes, precisamos converter um tipo de dado para outro, como transformar texto em número ou número em texto.
 Exemplos:
| # int para string |
| idade = 20 |

| idade_str = str(idade) |
| # string para int |

| numero = int("10") |
| # float para int (perde a parte decimal) |
| altura = int(1.75) |

| # int para float |
| peso = float(64) |

| # string para float |
| valor = float("3.14") |
Importante: ao converter string para número, o texto deve conter apenas dígitos, ou o Python dará erro.
“#” é utilizada para fazer comentários, válidos apenas para quem está programando, a máquina não os entende.
\033[0m''')

        escolha_pymod02 = input('\033[36mDigite 0 para voltar:  \033[m')
        if escolha_pymod02 == '0':
            break
        else:
            escolha_pymod02 = input('\033[36mEscolha inválida \033[m')
def modpython03():
    while True:
        print('\033[35m ==========\033[0m' ' \033[1;36m MODULO 03 \033[0m' '\033[35m ==========\033[0m')
        sleep(2.0)
        print('\033[36mOPERADORES EM PYTHON\033[0m')
        print('''\033[36m
Neste módulo, vamos aprender como fazer operações matemáticas, comparações e como usar operadores lógicos 
para criar condições mais inteligentes nos seus programas.

1. Operadores Aritméticos
Usados para fazer contas matemáticas com números (int ou float).
Operador	Nome
+	        Adição	
-	        Subtração	
*	        Multiplicação	
/	        Divisão (float)	
//	        Divisão inteira	
%	        Módulo (resto)	
**	        Potência	
Exemplos:
| soma = 10 + 5 |
| divisao_inteira = 9 // 2 |
| potencia = 3 ** 2 |

2. Operadores de Comparação
Usados para comparar valores. Sempre retornam True ou False.
Operador	Significado	
==	        Igual  a	Ex.: 5 == 5	 True
!=	        Diferente de	Ex.: 5 != 3	True
> 	        Maiorque	Ex.: 5 > 3	True
<	        Menor que	Ex.: 5 < 3	False
>=	        Maior ou igual    Ex.: 5 >= 5	 True
<=	        Menor ou igual	Ex.: 6 <= 4	 False
 Exemplo:
| idade = 18 |
| maior_de_idade = idade >= 18  # True |

3. Operadores Lógicos
Usados para combinar condições (muito usados em if e while).
Operador	Significado	
and	         E (ambas verdadeiras)   Ex.: True and False = False
or	         OU (uma ou ambas)       Ex.: True or False = True
not	         NÃO (inverte valor)	 Ex.: not True = False
Exemplo:
idade = 20
| tem_carteira = True |
| pode_dirigir = idade >= 18 and tem_carteira  # True |

DICA: O operador ‘AND’ terá como resultado verdadeiro apenas se ambas as condições forem verdadeiras.
Caso contrário, o resultado será falso.
O operador ‘OR’ terá como resultado falso apenas se ambas as condições forem falsas. Em todos os outros 
casos, o resultado será verdadeiro.
\033[0m''')

        escolha_pymod03 = input('\033[36mDigite 0 para voltar:  \033[m')
        if escolha_pymod03 == '0':
            break
        else:
            escolha_pymod03 = input('\033[36mEscolha inválida \033[m')
def modpython04():
    while True:
        print('\033[35m ==========\033[0m' ' \033[1;36m MODULO 04 \033[0m' '\033[35m ==========\033[0m')
        sleep(2.0)
        print('\033[36mENTRADA E SAÍDA DE DADOS\033[0m')
        print('''\033[36m
Neste módulo, você aprenderá como:
Pedir informações do usuário com input();
Mostrar resultados na tela com print();
Deixar sua saída mais bonita com formatação de strings.

1. Entrada de dados – input()
A função input() serve para ler dados do usuário via teclado.
O valor retornado sempre é uma string (texto), mesmo que o usuário digite números.
Exemplo:
| nome = input("Qual seu nome? ") |
| print("Olá,", nome) |
Conversão após o input:
| idade = int(input("Digite sua idade: ")) |
| altura = float(input("Digite sua altura: ")) |

 2. Saída de dados – print()
A função print() mostra mensagens ou valores na tela.
Exemplo:
| print("Seja bem-vindo!") |
| print("A soma de 2 + 2 é", 2 + 2) |

3. Formatação de Strings
Usamos a formatação para exibir variáveis dentro de frases com mais clareza.
 a) f-strings (forma moderna e prática — Python 3.6+)
| nome = "Luna" |
| idade = 22 |
| print(f"{nome} tem {idade} anos.") |
b) .format() (forma tradicional, compatível com versões antigas)
| print("{} tem {} anos.".format(nome, idade)) | 

 c) Formatação com casas decimais:
| preco = 5.6789 |
| print(f"Preço: R$ {preco:.2f}")  # R$ 5.68 |
\033[0m''')
        escolha_pymod04 = input('\033[36mDigite 0 para voltar:  \033[m')
        if escolha_pymod04 == '0':
            break
        else:
            escolha_pymod04 = input('\033[36mEscolha inválida \033[m')
def modpython05():
    while True:
        print('\033[35m ==========\033[0m' ' \033[1;36m MODULO 05 \033[0m' '\033[35m ==========\033[0m')
        sleep(2.0)
        print('\033[36mESTRUTURAS DE DECISÃO – IF, ELIF, ELSE\033[0m')
        print('''\033[36m
Estruturas de decisão permitem que o programa tome decisões diferentes com base em condições.
1. A estrutura 'if'
Executa um bloco de código somente se a condição for verdadeira (True).
Exemplo:
| idade = 20 |
| if idade >= 18: |
|    print("Você é maior de idade.") |
Dica: O bloco dentro do if precisa estar identado (recuado com tab ou 4 espaços).

2. A estrutura 'if + else'
Usada para escolher entre dois caminhos: se a condição for falsa, executa o else.
Exemplo:
| idade = 16 |
| if idade >= 18: |
|    print("Maior de idade.") |
| else: |
|    print("Menor de idade.") |

3. A estrutura 'if + elif + else'
Usada quando há várias condições diferentes. O elif significa “senão, se...”.
Exemplo:
| nota = 7 |
| if nota >= 9: |
|    print("Ótimo!") |
| elif nota >= 7: |
|    print("Bom!") |
| elif nota >= 5: |
|    print("Regular") |
| else: |
|    print("Reprovado.") |

4. Operadores que ajudam nas decisões
Você pode usar operadores de comparação e lógicos nas condições do if.
 Exemplo:
| idade = 18 |
| tem_carteira = True |
| if idade >= 18 and tem_carteira: |
|    print("Pode dirigir.") |
| else: |
|    print("Não pode dirigir.") |
\033[0m''')
        escolha_pymod05 = input('\033[36mDigite 0 para voltar:  \033[m')
        if escolha_pymod05 == '0':
            break
        else:
            escolha_pymod05 = input('\033[36mEscolha inválida \033[m')
def modpython06():
    while True:
        print('\033[35m ==========\033[0m' ' \033[1;36m MODULO 06 \033[0m' '\033[35m ==========\033[0m')
        sleep(2.0)
        print('\033[36mESTRUTURAS DE REPETIÇÃO\033[0m')
        print('''\033[36m
Este módulo ensina como repetir comandos automaticamente, sem ter que escrever várias vezes a mesma linha
de código. Isso é feito com as estruturas while e for.

1. while: repete enquanto a condição for verdadeira
A estrutura while é usada quando não sabemos quantas vezes o código será repetido. Ela repete um bloco de 
código enquanto a condição for verdadeira.
Exemplo:
| contador = 1 |
| while contador <= 5: |
|    print(f"Número: {contador}") |
|    contador += 1  # aumenta 1 a cada repetição |

O que acontece aqui:
Começa com contador = 1
Enquanto contador for menor ou igual a 5, o programa imprime o número
Depois, ele soma +1 em contador
Quando contador chega em 6, a condição fica falsa e o laço para
Cuidado com loops infinitos!
Se você esquecer de atualizar a variável dentro do while, o código pode nunca parar.
| # ERRADO - loop infinito! |
| x = 0
| while x < 5:
|    print(x)
|   # x não muda, então repete pra sempre!

2. for: ideal para repetições com quantidade conhecida
O for é ótimo quando você já sabe quantas vezes deseja repetir algo. Ele funciona com listas,
strings ou com a função range() (que cria uma sequência de números).
Exemplo com range():
| for i in range(1, 6): |
|    print(f"Passo: {i}") |
Aqui o que acontece:
•	range(1, 6) gera os números: 1, 2, 3, 4, 5 
•	O for roda uma vez para cada número
3. A função range()
A função range() gera uma sequência de números. É muito usada com for.
Formato:
| range(início, fim, passo) |
início: número inicial (opcional, padrão é 0) 
fim: onde para (não inclui esse número!) 
passo: de quantos em quantos (opcional) 
Exemplos:
| range(5)         # 0, 1, 2, 3, 4 |
| range(1, 6)      # 1, 2, 3, 4, 5 |
| range(10, 0, -2) # 10, 8, 6, 4, 2 |

4. A função enumerate()
O enumerate() é usado em conjunto com o for para pegar o índice e o valor de uma lista ao mesmo 
tempo.
Exemplo:
| nomes = ["Ana", "Bruno", "Carlos"] |
| for i, nome in enumerate(nomes): |
|    print(f"{i} - {nome}") |
Saída:
| 0 – Ana |
| 1 – Bruno |
| 2 – Carlos |
Isso é útil para numerar itens, criar menus, etc.
\033[0m''')
        escolha_pymod06 = input('\033[36mDigite 0 para voltar:  \033[m')
        if escolha_pymod06 == '0':
            break
        else:
            escolha_pymod06 = input('\033[36mEscolha inválida \033[m')
def modpython07():
    while True:
        print('\033[35m ==========\033[0m' ' \033[1;36m MODULO 07 \033[0m' '\033[35m ==========\033[0m')
        sleep(2.0)
        print('\033[36mFUNÇÕES\033[0m')
        print('''\033[36m
Funções são blocos de código reutilizáveis. Elas ajudam a organizar o programa e evitar repetições.
1. Definindo funções com def
Para criar uma função em Python, usamos a palavra-chave def, seguida do nome da função e parênteses ().
Exemplo simples:
| def saudacao(): |
|    print("Olá! Seja bem-vindo ao curso de Python!") |
Para executar a função, basta chamá-la pelo nome:
| saudacao() |

2. Parâmetros e retorno
Funções podem receber dados (parâmetros) e devolver resultados (com return).
Exemplo com parâmetros:
| def apresentar(nome): |
|    print(f"Olá, {nome}!") |
apresentar("Ana")  # Olá, Ana! 

Exemplo com retorno:
| def somar(a, b): |
|    return a + b |
| resultado = somar(3, 5) |
| print(f"Resultado: {resultado}")  # Resultado: 8 |
return envia o resultado da função de volta para quem a chamou.

3. Funções integradas (built-in)
O Python já vem com várias funções prontas que você pode usar a qualquer momento. Vamos ver algumas das mais usadas:

Função	O que faz	
print()	Exibe algo na tela	Ex.: print("Oi")
len()	Conta quantos itens tem uma lista ou string	Ex.: len("Python") → 6
sum()	Soma todos os números de uma lista	Ex.: sum([1, 2, 3]) → 6
max()	Retorna o maior valor	Ex.: max(10, 20, 5) → 20
min()	Retorna o menor valor	Ex.: min(3, 1, 9) → 1
type()	Mostra o tipo de dado	Ex.: type(5) → <class 'int'>
input()	Lê uma entrada do usuário	Ex.: nome = input("Seu nome: ")
\033[0m''')
        escolha_pymod07 = input('\033[36mDigite 0 para voltar:  \033[m')
        if escolha_pymod07 == '0':
            break

        else:
            escolha_pymod07 = input('\033[36mEscolha inválida \033[m')
def modpython08():
    while True:
        print('\033[35m ==========\033[0m' ' \033[1;36m MODULO 08 \033[0m' '\033[35m ==========\033[0m')
        sleep(2.0)
        print('\033[36mMANIPULAÇÃO DE ARQUIVOS (BÁSICO)\033[0m')
        print('''\033[36m
Neste módulo, vamos aprender a abrir, ler e escrever arquivos de texto (.txt) usando Python.
1. Abrindo arquivos com open()
A função open() é usada para acessar arquivos. Ela pode abrir arquivos para leitura, escrita 
ou adição de conteúdo.
Sintaxe:
| open("nome_do_arquivo.txt", "modo") |
        Modo	               Ação
"r"	leitura (read)     –      padrão
"w"	escrita (write)    –   sobrescreve o conteúdo
"a"	acrescenta (append) – adiciona no final
"x"	cria um novo arquivo (erro se já existir)

2. Lendo arquivos
Exemplo:
| arquivo = open("exemplo.txt", "r") |
| conteudo = arquivo.read() |
| print(conteudo) |
| arquivo.close() |
| read() lê todo o conteúdo do arquivo. |

Ler linha por linha:
| arquivo = open("exemplo.txt", "r") |
| for linha in arquivo: |
|    print(linha.strip())  # .strip() remove o \n – quebra de linha |
| arquivo.close() |

3. Escrevendo arquivos com .write()
Exemplo:
arquivo = open("novo.txt", "w")
arquivo.write("Primeira linha do arquivo.\n")
arquivo.write("Segunda linha.")
arquivo.close()
OBS: Com o modo "w", o conteúdo anterior é apagado!

4. Adicionando conteúdo com "a" (append)
Exemplo:
| arquivo = open("novo.txt", "a") |
| arquivo.write("\nNova linha adicionada.") | 
| arquivo.close() |

5. Usando with open() (forma recomendada)
Usar with garante que o arquivo será fechado automaticamente.
|with open("exemplo.txt", "r") as arquivo: |
|    print(arquivo.read()) |
Boa prática para evitar erros de arquivos abertos por muito tempo.

6. Fechando arquivos com .close()
Sempre que você usa open() para abrir um arquivo, é importante fechá-lo depois de terminar 
a leitura ou escrita. Isso é feito com o método .close().
Exemplo:
| arquivo = open("dados.txt", "r") |
| conteudo = arquivo.read() |
| arquivo.close() |

Por que usar .close()?
Libera recursos do sistema;
Garante que todas as alterações feitas no arquivo sejam salvas corretamente;
Evita erros, como tentar abrir o mesmo arquivo duas vezes ao mesmo tempo.

Dica:
Usar with open() já cuida disso automaticamente, sem precisar escrever .close():
| with open("dados.txt", "r") as arquivo: |
|    print(arquivo.read())  # O arquivo será fechado automaticamente aqui |
\033[0m''')
        escolha_pymod08 = input('\033[36mDigite 0 para voltar:  \033[m')
        if escolha_pymod08 == '0':
            break
        else:
            escolha_pymod08 = input('\033[36mEscolha inválida \033[m')
def admin():
    dados = carregar_dados()
    print("\n\033[34m==== ÁREA ADMINISTRATIVA ====\033[0m")

    # Contador de acessos por curso
    total_frequencias = {"Pensamento": 0, "Segurança": 0, "Python": 0}
    todas_idades = []
    notas_por_curso = {"Pensamento": [], "Segurança": [], "Python": []}
    conclusoes = {"Pensamento": 0, "Segurança": 0, "Python": 0}
    total_usuarios = len(dados)

    for aluno in dados:
        idade = int(aluno.get("idade", 0))
        todas_idades.append(idade)

        # Frequência por curso
        freq = aluno.get("frequencia", {})
        for curso in total_frequencias:
            total_frequencias[curso] += freq.get(curso, 0)

        # Notas
        for nota in aluno.get("notas", []):
            modulo = nota["modulo"]
            if "Pensamento" in modulo:
                notas_por_curso["Pensamento"].append(nota["nota"] / nota["total"] * 10)
            elif "Segurança" in modulo:
                notas_por_curso["Segurança"].append(nota["nota"] / nota["total"] * 10)
            elif "Python" in modulo:
                notas_por_curso["Python"].append(nota["nota"] / nota["total"] * 10)

        # Sistema de conclusão
        if "notas" in aluno:
            for curso in ["Pensamento", "Segurança", "Python"]:
                questoes = [n for n in aluno["notas"] if curso in n["modulo"]]
                if len(questoes) >= 2:
                    media = sum(n["nota"]/n["total"]*10 for n in questoes) / len(questoes)
                    if media >= 6:
                        conclusoes[curso] += 1

    # Mostrar curso mais acessado
    mais_acessado = max(total_frequencias, key=total_frequencias.get)
    print(f"\033[36mCurso mais visitado:\033[0m {mais_acessado} ({total_frequencias[mais_acessado]} acessos)")

    # Idades
    print(f"\033[36mIdades cadastradas:\033[0m {todas_idades}")

    # Notas por curso
    for curso, lista in notas_por_curso.items():
        if lista:
            media = sum(lista) / len(lista)
            print(f"\033[36mMédia de notas em {curso}:\033[0m {media:.2f}")
        else:
            print(f"\033[33mSem notas registradas para {curso}\033[0m")

    # Espera comando do admin
    comando = input("\n\033[36mDigite 'resumo' para ver estatísticas gerais ou 'sair' para voltar:\033[0m ").strip().lower()

    if comando == "resumo":
        from statistics import mean, mode

        try:
            media_idade = mean(todas_idades)
            moda_idade = mode(todas_idades)
        except:
            media_idade = moda_idade = "N/A"

        print("\n\033[34m==== ESTATÍSTICAS GERAIS ====\033[0m")
        print(f"\033[36mMédia de idades:\033[0m {media_idade}")
        print(f"\033[36mModa de idades:\033[0m {moda_idade}")

        for curso, lista in notas_por_curso.items():
            if lista:
                media = sum(lista) / len(lista)
                taxa = (conclusoes[curso] / total_usuarios) * 100 if total_usuarios > 0 else 0
                print(f"\033[36m{curso}:\033[0m média de {media:.2f} | taxa de conclusão: {taxa:.1f}%")
            else:
                print(f"\033[33m{curso}: Sem dados.\033[0m")

while True:
    escolha = menu()

    if usuario_logado:
        if escolha == '1':
            print('\033[36mVocê escolheu Cursos\033[0m')
            cursos_menu()
            # aqui entra a função de cursos com login
        elif escolha == '2':
            # aqui entra a função de segurança
            seguranca()
        elif escolha == '3':
            logout()       
        elif escolha == '4':
            minhas_informacoes()
        elif escolha == '0':
            print('\033[31mSaindo...\033[0m')
            break

        else:
            print('\033[31mOpção inválida!\033[0m')
    else:
        if escolha == '1':
            cadastro()
        elif escolha == '2':
            login()
        elif escolha == '3':
            cursos_menu()
        elif escolha == '4':
            # info geral
            seguranca()
        elif escolha == '0':
            print('\033[31mSaindo...\033[0m')
            break
        elif escolha == '@dm':
            admin()
        else:
            print('\033[31mOpção inválida!\033[0m')

    sleep(1.5)

