<template>
  <v-app style="background-color: #c4cbca">
    <Header />
    <v-main>
      <router-view />
    </v-main>
    <Footer />
  </v-app>
</template>

<script>
import Footer from "./components/Footer.vue";
import Header from "./components/Header.vue";
export default {
  name: "App",
  components: { Header, Footer },
};
</script>
