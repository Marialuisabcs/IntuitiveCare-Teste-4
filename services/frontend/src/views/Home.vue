<template>
  <div>
    <SeeMoreModal
      v-if="seeMoreDialog"
      :seeMoreDialog="seeMoreDialog"
      :closeDialog="closeDialog"
      :item="currentItem"
    />
    <Tip />
    <div
      class="d-flex mx-6"
      v-bind:class="page == 1 ? 'justify-end' : 'justify-space-between'"
    >
      <v-btn v-if="page != 1" @click="prevPage" color="primary">
        <v-icon left> mdi-arrow-left </v-icon>
        Anterior
      </v-btn>
      <v-btn @click="nextPage" color="primary">
        Próximo
        <v-icon right> mdi-arrow-right </v-icon>
      </v-btn>
    </div>
    <v-card class="rounded elevation-5 my-5 mx-5">
      <v-card-title>
        <p class="primary--text font-weight-black">RELATÓRIO CADOP</p>
        <v-spacer />
        <div class="d-flex justify-end">
          <v-text-field
            v-model="search"
            label="Buscar"
            :append-icon="'mdi-magnify'"
            :append-outer-icon="search ? 'mdi-close' : ''"
            @click:append="searchValues"
            @click:append-outer="cleanSearch"
            @keyup.enter="searchValues"
            color="primary"
            class="mx-4"
          />
          <v-autocomplete
            v-model="filter"
            :items="filters"
            clearable
            placeholder="Escolha um Filtro"
            @keyup.enter="searchValues"
          ></v-autocomplete>
        </div>
      </v-card-title>

      <v-data-table
        :headers="headers"
        :items="values"
        :items-per-page="10"
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
                color="icon"
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
      search: null,
      headers: [],
      seeMoreDialog: false,
      currentItem: {},
      values: [],
      page: 1,
      filters: ["registro", "cnpj", "nome_fantasia", "representante"],
      filter: null,
    };
  },
  cadopService: null,
  created() {
    this.cadopService = new CadOP();
  },
  mounted() {
    this.cadopService
      .getOperadoras()
      .then((data) => (this.values = data))
      .then(() => (this.loading = false));
    this.headers = this.cadopService.getHeaders();
  },
  methods: {
    seeMore(item) {
      this.seeMoreDialog = true;
      this.currentItem = item;
    },
    closeDialog() {
      this.seeMoreDialog = false;
    },
    nextPage() {
      this.page = this.page + 1;
      this.cadopService
        .getOperadoras(this.page, this.filter, this.search)
        .then((data) => (this.values = data))
        .then(() => (this.loading = false));
    },
    prevPage() {
      this.page = this.page - 1;
      this.cadopService
        .getOperadoras(this.page, this.filter, this.search)
        .then((data) => (this.values = data))
        .then(() => (this.loading = false));
    },
    searchValues() {
      this.loading = true;
      this.page = 1;
      this.cadopService
        .getOperadoras(this.page, this.filter, this.search)
        .then((data) => (this.values = data))
        .then(() => (this.loading = false));
    },
    cleanSearch() {
      location.reload();
    },
  },
  components: { SeeMoreModal, Tip },
};
</script>
