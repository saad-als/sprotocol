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

            <footer className='w-100 p-4 text-center '>
                < MessageBox />

            </footer>

        </>
    );

}

export default ChatPage