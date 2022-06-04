export default class CadOP {
  async getOperadoras(page = 1, filter = null, query = null) {
    if (filter != null) {
      const res = await fetch(
        "http://127.0.0.1:8000/?page=" +
          page +
          "&filterBy=" +
          filter +
          "&query=" +
          query
      ).catch((error) => {
        return error;
      });
      const data = await res.json();
      return data;
    }
    const res = await fetch("http://127.0.0.1:8000/?page=" + page).catch(
      (error) => {
        return error;
      }
    );
    const data = await res.json();
    return data;
  }

  getHeaders() {
    const headers = [
      { text: "id", value: "id" },
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
