<template>
    <div class="max-w-7xl mx-auto grid grid-cols-2 gap-4">
        <div class="main-left">
            <div class="p-12 bg-white border border-gray-200 rounded-lg">
                <h1 class="mb-6 text-2xl">Sign up</h1>

                <p class="mb-6 text-gray-500">
                    Join Flock and connect with friends, share your experiences, and discover a world of new possibilities.
                    Sign up today to start your journey with us!
                </p>

                <p class="font-bold">
                    Already have an account? <RouterLink :to="{'name': 'login'}"  class="underline">Click here</RouterLink> to log in!
                </p>
            </div>
        </div>  

        <div class="main-right">
            <div class="p-12 bg-white border border-gray-200 rounded-lg">
                <form class="space-y-6">
                    <div>
                        <label>First Name</label><br>
                        <input type="text" placeholder="Your first name" class="w-full mt-2 py-4 px-6 border border-gray-200 rounded-lg">
                    </div>

                    <div>
                        <label>Last Name</label><br>
                        <input type="text" placeholder="Your last name" class="w-full mt-2 py-4 px-6 border border-gray-200 rounded-lg">
                    </div>

                    <div>
                        <label>E-mail</label><br>
                        <input type="email" placeholder="Your e-mail address" class="w-full mt-2 py-4 px-6 border border-gray-200 rounded-lg">
                    </div>

                    <div>
                        <label>Password</label><br>
                        <input type="password" placeholder="Your password" class="w-full mt-2 py-4 px-6 border border-gray-200 rounded-lg">
                    </div>

                    <div>
                        <label>Repeat password</label><br>
                        <input type="password" placeholder="Repeat your password" class="w-full mt-2 py-4 px-6 border border-gray-200 rounded-lg">
                    </div>

                    <div>
                        <button class="py-4 px-6 bg-green-500 text-white rounded-lg">Sign Up</button>
                    </div>
                </form>
            </div>
        </div>
    </div>
</template>