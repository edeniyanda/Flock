<template>
    <div class="max-w-md mx-auto p-6 bg-white border border-gray-200 rounded-lg">
        <h1 class="text-2xl font-bold mb-6">Log In</h1>

        <form class="space-y-6">
            <div>
                <label for="email" class="block text-gray-700">E-mail</label>
                <input type="email" id="email" placeholder="Your e-mail address" class="w-full mt-1 py-3 px-4 border border-gray-300 rounded-lg" required>
            </div>

            <div>
                <label for="password" class="block text-gray-700">Password</label>
                <input type="password" id="password" placeholder="Your password" class="w-full mt-1 py-3 px-4 border border-gray-300 rounded-lg" required>
            </div>

            <div>
                <button type="submit" class="py-4 px-6 bg-green-500 text-white rounded-lg w-full">Log In</button>
            </div>
        </form>

        <p class="mt-6 text-gray-500 text-center">
            Don't have an account? 
            <RouterLink :to="{'name': 'signup'}" class="text-green-500 underline">Create one here</RouterLink>
        </p>
    </div>
</template>
