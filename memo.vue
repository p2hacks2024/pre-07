<script>
import SelectPostView from '@/components/SelectPostView.vue'
import { endpoint } from '~/components/APIEndPoint';

export default {
    data() {
        return {
            ids: [],
            selectedItems: [],
            rotate_angle: 0,
            isCenterCircleClicked: false
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
            const radius = 100
            const x = Math.cos((angle * Math.PI) / 180) * radius
            const y = Math.sin((angle * Math.PI) / 180) * radius
            return {
                left: `calc(50% + ${x}px)`,
                top: `calc(50% + ${y}px)` 
            }
        },
        handleCenterCircleClick() {
            this.isCenterCircleClicked = true;
        }
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
            this.rotate_angle += 1;
        }, 100); // 1秒ごとにrotate_angleを1増加
    }
}
</script>

<template>
    <div class="timeLine" :class="{ 'overlay': isCenterCircleClicked }">
        <div v-for="id in ids" :key="id" class="postContents">
            <SelectPostView class="postView" :id="id" @item-click="handleItemClick(id, $event)"/>
        </div>
        <div class="circle">
            <img class="center-circle" src="@/assets/balloon.png" alt="circle" @click="handleCenterCircleClick">
            <div v-for="(item, index) in selectedItems" :key="index" :style="getCirclePosition(index, selectedItems.length)" class="item">
                {{ item.title }}
            </div>
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
.timeLine.overlay {
    background-color: rgba(128, 128, 128, 0.5);
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    display: flex;
    justify-content: center;
    align-items: center;
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
}
.center-circle {
    width: 130px;
    height: 130px;
    /* transform: translateX(-225px) translateY(-250px); */
    opacity: 0.9;
    transition: transform 0.5s ease;
}
.timeLine.overlay .center-circle {
    transform: translate(-50%, -50%);
    position: fixed;
    top: 50%;
    left: 50%;
    z-index: 20;
}
.item {
    position: absolute;
    width: 50px;
    height: 50px;
    transform: translateX(-25px) translateY(-25px);
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