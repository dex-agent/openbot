# LIXEIRA — openbot

Residuo desta arqueologia. Apenas metadados sanitizados; nenhum conteudo de
usuario, segredo ou payload privado.

| Item | Origem | Motivo | Destino |
| --- | --- | --- | --- |
| `graphify-rebuild.lock.stale` | `graphify-out/.rebuild.lock` | lock de rebuild deixado por processo encerrado (clustering travado) | mantido como evidencia do incidente; o `graphify update --no-cluster` recria o lock quando precisa |
