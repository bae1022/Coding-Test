package KAKAO_BLIND_RECRUIMENT;

public class 신규아이디추천 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub

		System.out.println(solution("...!@BaT#*..y.abcdefghijklm"));
		System.out.println(solution("z-+.^."));
		System.out.println(solution("=.="));
		System.out.println(solution("123_.def"));
		System.out.println(solution("abcdefghijklmn.p"));
	}

	public static String solution(String new_id) {
		String answer = "";

		String step1 = new_id.toLowerCase(); // 소문자 변환

		String step2 = "";
		String[] ss = step1.split("");

		for (int i = 0; i < ss.length; i++){ // 알파벳, 소문자, 빼기, 밑줄, 등 뺌
			String temp = ss[i];
			char temp_c = temp.charAt(0);

			if (temp.equals("-") || temp.equals("_") || temp.equals(".") || Character.isDigit(temp_c) || Character.isLowerCase(temp_c)){
				step2 += temp;
			}
		}

		String step3 = step2.replace("..", ".");
		while (step3.contains("..")){
			step3 = step3.replace("..", ".");
		}

		String step4 = step3;
		if (step4.length() > 0){
			if (step4.startsWith(".")){
				step4 = step4.substring(1, step4.length());
			}
			if (step4.endsWith(".")){
				step4 = step4.substring(0, step4.length() - 1);
			}
		}

		String step5 = step4;
		if (step5.equals("")){
			step5 += "a";
		}

		String step6 = step5;
		if (step6.length() >= 16){
			step6 = step6.substring(0, 15);

			if (step6.endsWith(".")){
				step6 = step6.substring(0, step6.length() - 1);
			}
		}

		String step7 = step6;
		if (step7.length() <= 2){
			String t = step7.substring(step7.length() - 1, step7.length());
			for (int i = 0; i < 3 - step7.length() + 1; i++){
				step7 += t;
			}
		}

		answer = step7;


		return answer;
	}


}
