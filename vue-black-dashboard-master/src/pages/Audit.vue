<template>
<div>

    <div id="app">
        <h1>Audit Your Transcript</h1>

        <div class="container">
            <!-- Upload! -->
            <form enctype="multipart/form-data">
                <h4>Upload your transcipt here</h4>
            <label class="text-reader">
                <input type="file" @change="loadTextFromFile">
            </label>
            </form>
            
        </div>
        <br><br><br>
        <div>
            <h1>Audit Results</h1>

            <h4>Major: {{this.transcript.major}}</h4> 
            <br><br>
            <base-table :data="auditedTranscript">
            <template slot="columns">
                <th>Requirement</th>
            </template>  
            <template slot-scope="{row}">
                <td>{{row.name}}</td>
                <td>
                    <base-table :data="row.complete">
                        <template slot="columns" >
                            <th>Completed Courses</th>
                        </template>
                        <template slot-scope="{row}">
                            
                            <td>{{row}}</td>
                        </template>
                    </base-table>
                </td>
                <td v-if="!row.requirement_met">
                    <base-table :data="row.incomplete">
                        <template slot="columns" >
                            <th>Incomplete Courses</th>
                        </template>
                        <template slot-scope="{row}">
                            
                            <td>{{row}}</td>
                        </template>
                    </base-table>
                </td>
                <td v-if="!row.requirement_met">{{row.remaining}} Remaining</td>
                <td v-else>Requirement Satisified</td>
     
            </template>    
            </base-table>
        </div>
    </div>

</div>
</template>
<script>
    import axios from 'axios';
      import { BaseTable } from "@/components";


    const BASE_URL = "http://localhost:5000"
    const STATUS = {
        INITIAL: 0,
        SAVING: 1,
        SUCCESS: 2,
        FAILED: 3
    }





    export default {

        components: {
            BaseTable
        },

        data() {
            return {
                transcript:{},
                auditedTranscript: [],
                auditInformation: {
                    columns: ["requirement"]
                }
            }
        },

        methods: {

            /**
             * This method is used by the fileChooser to handle when a user submits a transcript!
             * @param event the event that occurs when a file is choosen
             */
            loadTextFromFile(event) {
                const file = event.target.files[0];


                const reader = new FileReader();

                reader.onload = e => this.$emit("load", e.target.result);
                reader.readAsText(file);

                reader.onload = event => {
                    this.transcript = JSON.parse(reader.result).transcript;
                    this.upload(JSON.parse(reader.result));
                }
            },
            /**
             * This function handles the uploading of form data to the backend
             */
                upload(formData) {
                const url = `${BASE_URL}/transcript`;
                return axios.post(url, formData)
                    // retrieve data
                    .then(res => {
                        return res.data;
                        })
                    .then(res => {

                        this.auditedTranscript = res;

                        console.log(this.auditedTranscript);
                    })
            }
        }
    }
</script>
<style lang="scss">
.dropbox {
    outline: 2px dashed grey; /* the dash box */
    outline-offset: -10px;
    background: lightcyan;
    color: dimgray;
    padding: 10px 10px;
    min-height: 200px; /* minimum height */
    position: relative;
    cursor: pointer;
  }

  .input-file {
    opacity: 0; /* invisible but it's there! */
    width: 100%;
    height: 200px;
    position: absolute;
    cursor: pointer;
  }

  .dropbox:hover {
    background: lightblue; /* when mouse over to the drop zone, change color */
  }

  .dropbox p {
    font-size: 1.2em;
    text-align: center;
    padding: 50px 0;
  }
</style>