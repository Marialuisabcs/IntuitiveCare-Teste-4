<template>
  <v-app style="background-color: #b2b1bc">
    <Header />
    <v-main>
      <router-view />
    </v-main>
  </v-app>
</template>

<script>
import Header from "./components/Header.vue";
export default {
  name: "App",
  data: () => ({
    //
  }),
  components: { Header },
};
</script>
