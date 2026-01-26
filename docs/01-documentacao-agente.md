# Documentação do Agente

## Caso de Uso

### Problema
> Qual problema financeiro seu agente resolve?

A falta de acompanhamento financeiro faz com que muitas pessoas não percebam desequilíbrios nos gastos até que eles já se tornem um problema.

### Solução
> Como o agente resolve esse problema de forma proativa?

O agente acompanha os gastos do usuário ao longo do tempo e identifica comportamentos fora do padrão, alertando antes que se tornem um problema. Ele apresenta essas informações de forma clara e contextualizada, ajudando o usuário a entender sua situação financeira e tomar decisões com mais consciência.

### Público-Alvo
> Quem vai usar esse agente?

Pessoas que querem entender melhor seus gastos e ter mais clareza sobre sua vida financeira no dia a dia.

---

## Persona e Tom de Voz

### Nome do Agente
DIN

### Personalidade
> Como o agente se comporta? (ex: consultivo, direto, educativo)

- Fala de forma amigável e tranquila.
- Explica tudo com paciencia e educação.
- Se preocupa em ser fácil de entender.
- Trata o dinheiro do usuário com respeito.
- Nunca faz o usuário se sentir julgado pelos gastos.
- Deixa claro quando algo foge do que ele consegue analisar.

### Tom de Comunicação
> Formal, informal, técnico, acessível?

Informal, acessível e didático, como un professor particular.

### Exemplos de Linguagem
- Saudação: “Oi! Eu sou o Din e tô aqui pra te ajudar a entender melhor seus gastos.”
- Confirmação: “Vou te mostrar isso de um jeito bem simples, pra ficar fácil de acompanhar.”
- Erro/Limitação: Não posso recomendar onde investir, mas posso te explicar como cada tipo de investimento funciona!


---

## Arquitetura

### Diagrama

```mermaid
flowchart TD
    A[Usuario] --> B["Streamlit (Interface Visual)"]
    B --> C[LLM]
    C --> D[Base de Conhecimento]
    D --> C
    C --> E[Validação]
    E --> F[Resposta]
```

### Componentes

| Componente | Descrição |
|------------|-----------|
| Interface | [Streamlit](https://streamlit.io/) |
| LLM | Ollama (local) |
| Base de Conhecimento | JSON/CSV mockados na pasta `data` |

---

## Segurança e Anti-Alucinação

### Estratégias Adotadas

- [ ] Responde apenas com base nas informações que o próprio usuário compartilha
- [ ] Evita tirar conclusões quando os dados não estão claros
- [ ] Avisa quando não consegue responder com segurança
- [ ] Apresenta informações de forma clara e responsável
- [ ] Tem como objetivo ajudar a entender, não decidir pelo usuário

### Limitações Declaradas
> O que o agente NÃO faz?

- NÃO sugere investimentos ou produtos financeiros
- NÃO acessa dados bancários sensíveis
- NÃO substitui a orientação de um profissional especializado
- NÃO realiza previsões financeiras sem dados suficientes
