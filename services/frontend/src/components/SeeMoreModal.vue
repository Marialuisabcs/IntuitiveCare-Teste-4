<template>
  <v-row justify="center">
    <v-dialog v-model="seeMoreDialog" persistent max-width="600px">
      <v-card>
        <v-card-title>
          <span class="text-h5">Registro Completo</span>
          <v-spacer></v-spacer>
          <v-btn color="blue darken-1" text @click="closeDialog">
            Voltar
          </v-btn>
        </v-card-title>
        <v-card-text>
          <v-container>
            <v-row>
              <v-col cols="12" sm="12" md="6">
                <v-text-field
                  v-model="item.registro_ans"
                  readonly
                  label="Registro ANS"
                ></v-text-field>
              </v-col>
              <v-col cols="12" sm="12" md="6">
                <v-text-field
                  v-model="item.cnpj"
                  readonly
                  label="CNPJ"
                ></v-text-field>
              </v-col>
              <v-col cols="12">
                <v-text-field
                  v-model="item.razao_social"
                  readonly
                  label="Razão Social"
                ></v-text-field>
              </v-col>
              <v-col cols="12" sm="12" md="6">
                <v-text-field
                  v-model="item.nome_fantasia"
                  readonly
                  label="Nome Fantasia"
                ></v-text-field>
              </v-col>
              <v-col cols="12" sm="12" md="6">
                <v-text-field
                  v-model="item.modalidade"
                  readonly
                  label="Modalidade"
                ></v-text-field>
              </v-col>
              <v-col cols="12">
                <v-text-field
                  v-model="item.logradouro"
                  readonly
                  label="Logradouro"
                ></v-text-field>
              </v-col>
              <v-col cols="12" sm="12" md="6">
                <v-text-field
                  v-model="item.complemento"
                  readonly
                  label="Complemento"
                ></v-text-field>
              </v-col>
              <v-col cols="12" sm="12" md="6">
                <v-text-field
                  v-model="item.numero"
                  readonly
                  label="Número"
                ></v-text-field>
              </v-col>
              <v-col cols="12" sm="12" md="6">
                <v-text-field
                  v-model="item.bairro"
                  readonly
                  label="Bairro"
                ></v-text-field>
              </v-col>
              <v-col cols="12" sm="12" md="6">
                <v-text-field
                  v-model="item.cidade"
                  readonly
                  label="Cidade"
                ></v-text-field>
              </v-col>
              <v-col cols="12" sm="12" md="4">
                <v-text-field
                  v-model="item.uf"
                  readonly
                  label="UF"
                ></v-text-field>
              </v-col>
              <v-col cols="12" sm="12" md="4">
                <v-text-field
                  v-model="item.cep"
                  readonly
                  label="CEP"
                ></v-text-field>
              </v-col>
              <v-col cols="12" sm="12" md="4">
                <v-text-field
                  v-model="item.ddd"
                  readonly
                  label="DDD"
                ></v-text-field>
              </v-col>
              <v-col cols="12" sm="12" md="6">
                <v-text-field
                  v-model="item.telefone"
                  readonly
                  label="Telefone"
                ></v-text-field>
              </v-col>
              <v-col cols="12" sm="12" md="6">
                <v-text-field
                  v-model="item.fax"
                  readonly
                  label="Fax"
                ></v-text-field>
              </v-col>
              <v-col cols="12">
                <v-text-field
                  v-model="item.representante"
                  readonly
                  label="Representante"
                ></v-text-field>
              </v-col>
              <v-col cols="12" sm="12" md="6">
                <v-text-field
                  v-model="item.endereco_eletronico"
                  readonly
                  label="Endereço Eletrônico"
                ></v-text-field>
              </v-col>
              <v-col cols="12" sm="12" md="6">
                <v-text-field
                  v-model="item.cargo"
                  readonly
                  label="Cargo"
                ></v-text-field>
              </v-col>
              <v-col cols="12">
                <v-text-field
                  v-model="item.data"
                  readonly
                  label="Data do registro"
                  prepend-icon="mdi-calendar"
                  hint="DD/MM/AA"
                  persistent-hint
                ></v-text-field>
              </v-col>
            </v-row>
          </v-container>
        </v-card-text>
        <v-card-actions>
          <v-spacer></v-spacer>
          <v-btn color="blue darken-1" text @click="closeDialog">
            Voltar
          </v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>
  </v-row>
</template>

<script>
export default {
  props: {
    seeMoreDialog: Boolean,
    closeDialog: Function,
    item: Object,
  },
};
</script>

<style></style>
