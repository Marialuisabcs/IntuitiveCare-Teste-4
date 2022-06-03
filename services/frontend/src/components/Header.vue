<template>
  <v-app-bar app color="primary">
    <v-toolbar-title class="white--text font-weight-bold">
      TESTE 4
    </v-toolbar-title>
    <v-spacer></v-spacer>
    <h1 class="terciary--text">MARIA LUÍSA</h1>
    <v-spacer></v-spacer>
    <a :href="url">
      <v-icon x-large color="white"> mdi-github </v-icon>
    </a>
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
