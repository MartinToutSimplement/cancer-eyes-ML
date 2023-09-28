<template>
    <div class="mainUpload">
        <input type="file" accept="image/*" @change="handleFileUpload" class="button">
        <div v-if="imageUrl">
            <img :src="imageUrl" class="image-preview" />
        </div>
    </div>
</template>
  
<script>
export default {
    name: 'ImageUploader',
    data() {
        return {
            imageUrl: null
        };
    },
    methods: {
        handleFileUpload(event) {
            const file = event.target.files[0];
            this.imageUrl = URL.createObjectURL(file);
            this.$emit('image-uploaded', file);
        }
    }
};
</script>
  
<style>
.button {
    display: inline-block;
    background-color: #7b38d8;
    border-radius: 10px;
    border: 4px double #cccccc;
    color: #eeeeee;
    text-align: center;
    font-size: 28px;
    padding: 20px;
    width: 200px;
    transition: all 0.5s;
    cursor: pointer;
    margin: 5px;
}

.button span {
    cursor: pointer;
    display: inline-block;
    position: relative;
    transition: 0.5s;
}

.button span:after {
    content: "\00bb";
    position: absolute;
    opacity: 0;
    top: 0;
    right: -20px;
    transition: 0.5s;
}

.button:hover {
    background-color: #f7c2f9;
}

.button:hover span {
    padding-right: 25px;
}

.button:hover span:after {
    opacity: 1;
    right: 0;
}

.image-preview {
    max-width: 300px;
    max-height: 300px;
}

.mainUpload {
    margin: 0;
    padding: 0;
    width: 50%;
}</style>