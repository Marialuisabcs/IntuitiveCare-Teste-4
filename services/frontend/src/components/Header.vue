<template>
  <v-app-bar app color="primary">
    <v-toolbar-title class="white--text font-weight-bold">
      TESTE 4 - API
    </v-toolbar-title>
    <v-spacer></v-spacer>
    <v-tooltip left>
      <template v-slot:activator="{ on, attrs }">
        <a :href="url" v-bind="attrs" v-on="on">
          <v-icon x-large color="white"> mdi-github </v-icon>
        </a>
      </template>
      <span>Ir para o repositório da aplicação</span>
    </v-tooltip>
  </v-app-bar>
</template>

<script>
export default {
  data() {
    return {
      url: "https://github.com/Marialuisabcs/IntuitiveCare-Teste-4.git",
    };
  },
};
</script>
