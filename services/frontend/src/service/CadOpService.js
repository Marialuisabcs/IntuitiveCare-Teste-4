export default class CadOP {
  getHeaders() {
    const headers = [
      { text: "Registro ANS", value: "registro_ans" },
      { text: "CNPJ", value: "cnpj" },
      { text: "Nome Fantasia", value: "nome_fantasia" },
      { text: "Modalidade", value: "modalidade" },
      { text: "UF", value: "uf" },
      { text: "Telefone", value: "telefone" },
      {
        text: "Endereço Eletrônico",
        value: "endereco_eletronico",
      },
      { text: "Representante", value: "representante" },
      { text: "Cargo Representante", value: "cargo" },
      { text: "Data Registro", value: "data" },
      { text: "Actions", value: "actions", sortable: false },
    ];
    return headers;
  }
}
