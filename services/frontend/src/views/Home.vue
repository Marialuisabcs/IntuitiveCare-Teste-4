<template>
  <div>
    <SeeMoreModal
      v-if="seeMoreDialog"
      :seeMoreDialog="seeMoreDialog"
      :closeDialog="closeDialog"
      :item="currentItem"
    />
    <Tip />
    <v-card class="rounded elevation-5 my-5 mx-5">
      <v-card-title>
        RELATÓRIO CADOP
        <v-spacer />
        <v-text-field v-model="search" label="Buscar" class="mx-4" />
      </v-card-title>

      <v-data-table
        :headers="headers"
        :items="dummyData"
        :items-per-page="5"
        :loading="loading"
        loading-text="Carregando..."
        disable-sort
        item-key="registr_ans"
        hide-default-footer
        class=""
      >
        <template v-slot:[`item.actions`]="{ item }">
          <v-tooltip bottom>
            <template v-slot:activator="{ on, attrs }">
              <v-icon
                color="secondary"
                v-bind="attrs"
                v-on="on"
                class="ml-2"
                @click="seeMore(item)"
              >
                mdi-plus-thick
              </v-icon>
            </template>
            <span>Ver registro completo</span>
          </v-tooltip>
        </template>
      </v-data-table>
    </v-card>
  </div>
</template>

<script>
// @ is an alias to /src
import CadOP from "../service/CadOpService";
import SeeMoreModal from "../components/SeeMoreModal.vue";
import Tip from "../components/Tip.vue";

export default {
  data() {
    return {
      loading: true,
      search: "",
      headers: [],
      seeMoreDialog: false,
      currentItem: {},
      dummyData: [
        {
          registro_ans: "418374",
          cnpj: "1,18281E+13",
          razao_social:
            "CAIXA DE ASSISTÊNCIA DO SETOR DE ENERGIA -EVIDA -ASSISTÊNCIA À SAÚDE",
          nome_fantasia: "E-VIDA",
          modalidade: "Autogestão",
          logradouro: "SETOR DE HABITAÇÕES COLETIVAS GEMINADAS",
          numero: "QUADRA 704/705",
          complemento: "BLOCO C, LOJA 48",
          bairro: "ASA NORTE",
          cidade: "Brasília",
          uf: "DF",
          cep: "70730630",
          ddd: "61",
          telefone: "39668300",
          fax: "39668302",
          endereco_eletronico: "governanca@evida.org.br",
          representante: "ELI PINTO DE MELO JUNIOR",
          cargo: "PRESIDENTE",
          data: "12/01/2012",
        },
      ],
    };
  },
  cadopService: null,
  created() {
    this.cadopService = new CadOP();
  },
  mounted() {
    this.headers = this.cadopService.getHeaders();
    this.loading = false;
  },
  methods: {
    seeMore(item) {
      this.seeMoreDialog = true;
      this.currentItem = item;
    },
    closeDialog() {
      this.seeMoreDialog = false;
    },
  },
  components: { SeeMoreModal, Tip },
};
</script>
