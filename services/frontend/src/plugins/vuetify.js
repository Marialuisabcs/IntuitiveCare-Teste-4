import Vue from "vue";
import Vuetify from "vuetify/lib/framework";

Vue.use(Vuetify);

const vuetify = new Vuetify({
  theme: {
    themes: {
      light: {
        primary: "#3CBBB1",
        secondary: "#C4CBCA",
        terciary: "#F0F0F0",
        icon: "#236C66", //b2b1bc
        //anchor
      },
    },
  },
});

export default vuetify;
