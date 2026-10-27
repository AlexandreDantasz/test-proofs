# Checklist de code review

Use em todo PR, inclusive nos seus. Escreva cada problema como comentário: linha, risco, sugestão.

## Requisito
- [ ] O código faz exatamente o que o requisito pede? (ex.: "mais de k" vs "pelo menos k")
- [ ] Mensagens de log e de erro dizem a verdade sobre o que foi checado?

## Entrada e erros
- [ ] Toda entrada externa é validada (null, vazio, formato)?
- [ ] Erro do cliente devolve 4xx e erro do servidor devolve 5xx?
- [ ] Nenhum `catch` genérico escondendo bugs?

## HTTP e assincronia
- [ ] O status bate com o comportamento? (202 só com fila de verdade)
- [ ] Operações lentas não prendem a requisição?

## Estado e concorrência
- [ ] Existe ordem obrigatória de chamadas (acoplamento temporal)?
- [ ] Duas requisições ao mesmo tempo podem compartilhar estado?
- [ ] Retry pode duplicar efeito? Há idempotência?

## Testes
- [ ] Há teste para o caso comum e para as bordas?
- [ ] Há teste que pegaria o bug que este PR corrige?
- [ ] A complexidade está adequada ao volume esperado?

## Código morto e clareza
- [ ] Nenhum `return` ou ramo que nunca executa?
- [ ] Nomes dizem o que a coisa faz?
