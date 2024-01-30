import NavBarChat from '../components/Chat/NavBarChat'
import MessageBubble from '../components/Chat/MessageBubble'
import MessageBox from '../components/Chat/MessageBox'

function ChatPage() {

    return (
        <>

            <NavBarChat />

            <div className="container-md">

                <MessageBubble />

            </div>

            <div className='p-4 container-md'>
                < MessageBox />

            </div>

        </>
    );

}

export default ChatPage