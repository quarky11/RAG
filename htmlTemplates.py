css = '''
<style>
body {
    background-color: #a8e6cf; /* Soft mint green */
}

.chat-message {
    padding: 1.5rem; 
    border-radius: 0.5rem; 
    margin-bottom: 1rem; 
    display: flex;
}

.chat-message.user {
    background-color: #b3cde0; /* Soft blue for user */
}

.chat-message.bot {
    background-color: #d1f8e5; /* Soft pastel green for bot */
}

.chat-message .avatar {
    width: 20%;
}

.chat-message .avatar img {
    max-width: 78px;
    max-height: 78px;
    border-radius: 50%;
    object-fit: cover;
}

.chat-message .message {
    width: 80%;
    padding: 0 1.5rem;
    color: #333; /* Darker text for better readability */
}
</style>
'''

bot_template = '''
<div class="chat-message bot">
    <div class="avatar">
        <img src="https://cdn.kyou.id/items/78056-jujutsu-kaisen-nesoberi-plush-itadori-yuji-s.jpg" style="max-height: 78px; max-width: 78px; border-radius: 50%; object-fit: cover;">
    </div>
    <div class="message">{{MSG}}</div>
</div>
'''

user_template = '''
<div class="chat-message user">
    <div class="avatar">
        <img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSqAjN7SpNDP9Oqpw_ya4vMuxrT-ISfzOMAqA&s">
    </div>    
    <div class="message">{{MSG}}</div>
</div>
'''
