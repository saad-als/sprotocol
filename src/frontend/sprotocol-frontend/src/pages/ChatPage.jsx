import NavBarChat from '../components/Chat/NavBarChat'
import MessageBubble from '../components/Chat/MessageBubble'
import MessageBox from '../components/Chat/MessageBox'

function ChatPage() {

    return (
        <>

            <NavBarChat />
            <div className="container-sm overflow-auto " style={{ height: 600 + 'px' }}>

                <MessageBubble />
                <MessageBubble />
                <MessageBubble />
                <MessageBubble />
                <MessageBubble />

            </div>

            <div className='p-4 container-md fixed-bottom'>
                < MessageBox />

            </div>

        </>
    );

}

export default ChatPage