<template>
  <div>
    <!-- <NuxtLink :to="{ name: 'estatisticas' }">estatistica</NuxtLink> -->
    <v-container>
      <v-layout row>
        <v-flex md8>
          <v-textarea
            style="margin-top: 10px"
            v-model="messages"
            label="Cole noticia para verificar"
          ></v-textarea> 

          <v-container px-0>
            <v-btn @click="cleanText">Limpar</v-btn>
            <v-btn @click="checkNews">Verificar</v-btn>
          </v-container>

          <v-card elevation="4">
            <div>
              <p>{{ predict.status }}</p>
              <p>{{ predict.proba }}</p>
            </div>
          </v-card>
        </v-flex>
        <v-flex md4>
          <v-btn  block class="primary">2</v-btn>
        </v-flex>
      </v-layout>
    </v-container>

  </div>
</template>

<script>
export default {
  name: "IndexPage",
  data() {
    return {
      messages: "",
      predict: { status: "", proba: "", result: false },
    };
  },
  methods: {
    async checkNews({ $axios }) {
      if (this.messages.length !== 0) {
        const article = { text: this.messages };
        const predict_post = await this.$axios.post(
          "https://api-backend-fake-news.herokuapp.com/news/only/predict",
          article
        );
        this.predict.status = predict_post.data.modelo;
        this.predict.proba = predict_post.data.proba;
        this.predict.result = true;
      } else {
        alert("Campo vazio");
      }
    },
    cleanText() {
      this.messages = "";
      this.predict.status = "";
      this.predict.proba = "";
      this.predict.result = false;
    },
  },

  async asyncData({ $axios }) {
    const news = await $axios.get("https://api-backend-fake-news.herokuapp.com/home")
    console.log(news.data)
    return {
      news: news.data
    }
  }
};
</script>
