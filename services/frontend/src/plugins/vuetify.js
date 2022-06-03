import Vue from "vue";
import Vuetify from "vuetify/lib/framework";

Vue.use(Vuetify);

const vuetify = new Vuetify({
  theme: {
    themes: {
      light: {
        primary: "#3a3d70",
        secondary: "#6c72d8",
        terciary: "#e238c4",
        background: "#b2b1bc", //b2b1bc
        //anchor
      },
    },
  },
});

export default vuetify;
