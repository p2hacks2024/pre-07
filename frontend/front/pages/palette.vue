<script>
import SelectPostView from '@/components/SelectPostView.vue'
import { endpoint } from '~/components/APIEndPoint';

export default {
    data() {
        return {
            ids: [],
            selectedItems: [],
            rotate_angle: 0,
            isMixMode: false,
            showPlalette: false,
            radius: 100,
            palette_data : {
                title: '',
                content: '',
            },
        }
    },
    methods: {
        handleItemClick(item, title) {
            this.selectedItems.push({ item, title });
            console.log(this.selectedItems);
        },
        getCirclePosition(index, total)  {
            if (total === 0) return { left: '50%', top: '50%' }
            const angle = (index * 360 / total) - 90 + this.rotate_angle
            const x = Math.cos((angle * Math.PI) / 180) * this.radius
            const y = Math.sin((angle * Math.PI) / 180) * this.radius
            return {
                left: `calc(50% + ${x}px)`,
                top: `calc(50% + ${y}px)` 
            }
        },
        handleMixMode() {
            console.log('mix mode')
            this.isMixMode = true
        },
    },
    async created() {
        const response = await fetch(endpoint + 'palette/', {
            method: 'GET',
            credentials: 'include'
        })
        const data = await response.json()
        this.ids = data
    },
    mounted() {
        setInterval(() => {
            this.rotate_angle += 0.3;
            if (this.isMixMode) {
                if (this.radius >= 0) {
                    this.radius -= 1;
                }
                else {
                    this.showPlalette = true
                }
            }
        }, 10); // 1秒ごとにrotate_angleを1増加
    }
}
</script>

<template>
    <div class="timeLine">
        <div v-for="id in ids" :key="id" class="postContents">
            <SelectPostView class="postView" :id="id" @item-click="handleItemClick(id, $event)"/>
        </div>
        <div :class="{ 'overlay': isMixMode }"></div>

        <div class="palette" :class="{'palette-show': showPlalette}">
            
        </div>

        <div class="circle" :class="{ 'center-move': isMixMode }">
            <div v-for="(item, index) in selectedItems" :key="index" :style="getCirclePosition(index, selectedItems.length)" class="item">
                {{ item.title }}
            </div>
            <img class="center-circle" src="@/assets/balloon.png" alt="circle" @click="handleMixMode">
        </div>
    </div>
</template>

<style scoped>
.timeLine {
    padding: 10px;
    background-color: #f3f3f3;
    display: flex;
    flex-wrap: wrap;
}
.palette {
    display: none;
}
.palette-show {
    display: block;
    position: fixed;
    top: 10%;
    left: 10%;
    width: 70%;
    max-height: 80%;
    background-color: rgb(255, 255, 255);
    z-index: 10;
    border-radius: 20px;
    padding: 5%;
}
.overlay {
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background-color: rgba(0, 0, 0, 0.5);
    z-index: 10;
}
.postContents {
    width: 50%;
}

.postView {
    margin: 5%;
}
.circle {
    position: fixed;
    left: 50%;
    top: 75%;
    transform: translateX(-65px) translateY(-65px);
    z-index: 11;
}
.center-circle {
    width: 130px;
    height: 130px;
    /* transform: translateX(-225px) translateY(-250px); */
    opacity: 0.9;
}
.center-move {
    transform: translate(-50%, -50%);
    transition: transform 1s ease;
    position: fixed;
    top: 50%;
    left: 50%;
}

.item {
    position: absolute;
    width: 80px;
    height: 80px;
    transform: translateX(-40px) translateY(-40px);
    border-radius: 50%;
    background-color: aqua;
    display: flex;
    justify-content: center;
    align-items: center;
    font-size: 20px;
    color: white;
    cursor: pointer;
}
</style>