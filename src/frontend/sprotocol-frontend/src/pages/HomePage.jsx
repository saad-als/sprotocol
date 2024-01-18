import NavBar from '../components/NavBar';
import LoginForm from '../components/LoginForm'
import '../styles/loginForm.css'
function HomePage() {

    return (
        <>



            <NavBar />
            <div className="container-md d-flex align-items-center justify-content-center w-50">

                <div className="p-4 m-4 shadow rounded-2 login-form">

                    <LoginForm />

                </div>


            </div>

            <footer className=' w-100 p-2 text-center text-body-tertiary'>@ 2024 Copyright: Saad Alsayed</footer>



        </>
    );

}


export default HomePage