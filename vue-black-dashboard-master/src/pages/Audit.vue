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
    </div>

</div>
</template>
<script>
    import axios from 'axios';


    const BASE_URL = "http://localhost:5000"
    const STATUS = {
        INITIAL: 0,
        SAVING: 1,
        SUCCESS: 2,
        FAILED: 3
    }





    export default {
        data() {
            return {
                auditedTranscript: {}
            }
        },

        methods: {
            loadTextFromFile(event) {
                const file = event.target.files[0];
                const reader = new FileReader();

                reader.onload = e => this.$emit("load", e.target.result);
                reader.readAsText(file);

                reader.onload = event => {
                    this.upload(JSON.parse(reader.result));
                }
            },
            /**
             * This function handles the uploading of form data to the backend
             */
                upload(formData) {
                const url = `${BASE_URL}/transcript`;
                console.log(formData)
                return axios.post(url, formData)
                    // retrieve data
                    .then(res => {
                        this.auditedTranscript = Object.assign({},res.data);
                        console.log(res);
                        })
                    .then(res => {
                        console.log(res);
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